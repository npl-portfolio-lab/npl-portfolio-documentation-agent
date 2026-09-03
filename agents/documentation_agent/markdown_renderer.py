from pathlib import Path

from .context_builder import build_documentation_context
from .models import UseCase


class MarkdownRenderer:

    def __init__(
        self,
        output_directory: Path = Path("docs/use_cases"),
    ):
        self.output_directory = output_directory

    def render_use_case(
        self,
        use_case: UseCase,
    ) -> Path:

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = self.output_directory / f"{use_case.id}.md"

        content = self._build_content(use_case)

        output_path.write_text(
            content,
            encoding="utf-8",
        )

        return output_path

    def _build_content(
        self,
        use_case: UseCase,
    ) -> str:

        context = build_documentation_context()

        actor_name = self._get_actor_name(
            use_case.primary_actor,
            context,
        )

        requirement_labels = [
            self._get_requirement_label(
                requirement_id,
                context,
            )
            for requirement_id in use_case.related_requirements
        ]

        business_rule_labels = [
            self._get_business_rule_label(
                rule_id,
                context,
            )
            for rule_id in use_case.business_rules
        ]

        preconditions = "\n".join(f"- {item}" for item in use_case.preconditions)

        main_flow = "\n".join(
            f"{index}. {item}"
            for index, item in enumerate(
                use_case.main_flow,
                start=1,
            )
        )

        alternative_flows = "\n".join(
            f"- {item}" for item in use_case.alternative_flows
        )

        postconditions = "\n".join(f"- {item}" for item in use_case.postconditions)

        related_requirements = "\n".join(f"- {item}" for item in requirement_labels)

        business_rules = "\n".join(f"- {item}" for item in business_rule_labels)

        return f"""# {use_case.id} - {use_case.name}

## Información general

**Identificador:** {use_case.id}

**Actor principal:** {use_case.primary_actor} - {actor_name}

## Objetivo

{use_case.objective}

## Precondiciones

{preconditions or "- No definidas."}

## Flujo principal

{main_flow or "No definido."}

## Flujos alternativos

{alternative_flows or "- No definidos."}

## Postcondiciones

{postconditions or "- No definidas."}

## Requerimientos relacionados

{related_requirements or "- No definidos."}

## Reglas de negocio

{business_rules or "- No definidas."}
"""

    def _get_actor_name(
        self,
        actor_id: str,
        context: dict,
    ) -> str:

        for actor in context["actors"]:
            if actor["id"] == actor_id:
                return actor["name"]

        return "Actor no encontrado"

    def _get_requirement_label(
        self,
        requirement_id: str,
        context: dict,
    ) -> str:

        for requirement in context["functional_requirements"]:
            if requirement["id"] == requirement_id:
                return f'{requirement["id"]} - ' f'{requirement["name"]}'

        return requirement_id

    def _get_business_rule_label(
        self,
        rule_id: str,
        context: dict,
    ) -> str:

        for rule in context["business_rules"]:
            if rule["id"] == rule_id:
                return f'{rule["id"]} - ' f'{rule["name"]}'

        return rule_id
