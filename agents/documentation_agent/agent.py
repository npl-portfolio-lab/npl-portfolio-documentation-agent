import json
from pathlib import Path

from .validators import validate_use_case_references
from .context_builder import build_documentation_context
from .llm_client import LLMClient
from .models import UseCase


class DocumentationAgent:

    def __init__(
        self,
        llm_client: LLMClient,
    ):
        self.llm_client = llm_client

    def _load_prompt_template(
        self,
    ) -> str:

        prompt_path = Path("prompts/use_case_prompt.txt")

        return prompt_path.read_text(encoding="utf-8")

    def generate_use_case(
        self,
        requirement_id: str,
    ) -> UseCase:

        context = build_documentation_context()

        # Obtener requerimientos funcionales
        requirements = context["functional_requirements"]

        # Buscar el requerimiento solicitado
        requirement = next(
            (item for item in requirements if item["id"] == requirement_id),
            None,
        )

        if requirement is None:
            raise ValueError(f"Requirement {requirement_id} not found")

        # Obtener definiciones detalladas
        # de casos de uso
        use_case_definitions = context["use_case_definitions"]

        # Buscar la definición asociada
        # al requerimiento
        use_case_definition = next(
            (
                item
                for item in use_case_definitions
                if (item["related_requirement"] == requirement_id)
            ),
            None,
        )

        if use_case_definition is None:
            raise ValueError(
                f"No use case definition found " f"for requirement {requirement_id}"
            )

        # Cargar instrucciones base
        # del agente
        prompt_template = self._load_prompt_template()

        # Construir contexto que recibirá
        # el modelo
        prompt = f"""
{prompt_template}

PROJECT:
{json.dumps(
    context["project"],
    indent=2,
    ensure_ascii=False
)}

AVAILABLE ACTORS:
{json.dumps(
    context["actors"],
    indent=2,
    ensure_ascii=False
)}

AVAILABLE BUSINESS RULES:
{json.dumps(
    context["business_rules"],
    indent=2,
    ensure_ascii=False
)}

REQUIREMENT TO DOCUMENT:
{json.dumps(
    requirement,
    indent=2,
    ensure_ascii=False
)}

USE CASE DEFINITION:
{json.dumps(
    use_case_definition,
    indent=2,
    ensure_ascii=False
)}
"""

        # Enviar prompt al LLM
        response = self.llm_client.generate(prompt)

        # Convertir JSON generado
        # a objeto Python
        data = json.loads(response)

        # Validación estructural
        # con Pydantic
        use_case = UseCase(**data)

        # Validar referencias
        # ACT / RF / RN
        validate_use_case_references(
            use_case=use_case,
            context=context,
        )

        return use_case
