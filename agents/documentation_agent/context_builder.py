from pathlib import Path

from .loader import (
    load_actors,
    load_architecture,
    load_business_rules,
    load_data_model,
    load_functional_requirements,
    load_use_case_definitions,
)
from .project_loader import load_project


def build_documentation_context() -> dict:
    """
    Construye el contexto completo utilizado por el agente
    de documentación a partir de las fuentes YAML del proyecto.
    """

    # Rutas de las fuentes estructuradas del proyecto.
    project_path = Path("requirements/project.yaml")
    requirements_path = Path("requirements/functional_requirements.yaml")
    actors_path = Path("requirements/actors.yaml")
    business_rules_path = Path("requirements/business_rules.yaml")
    use_case_definitions_path = Path("requirements/use_case_definitions.yaml")
    architecture_path = Path("requirements/architecture.yaml")
    data_model_path = Path("requirements/data_model.yaml")

    # Carga y validación mediante los loaders.
    project = load_project(project_path)

    functional_requirements = load_functional_requirements(requirements_path)

    actors = load_actors(actors_path)

    business_rules = load_business_rules(business_rules_path)

    use_case_definitions = load_use_case_definitions(use_case_definitions_path)

    architecture = load_architecture(architecture_path)

    data_model = load_data_model(data_model_path)

    # Construcción del contexto serializable que utilizará
    # el agente de documentación.
    return {
        "project": project,
        "functional_requirements": [
            requirement.model_dump() for requirement in functional_requirements
        ],
        "actors": [actor.model_dump() for actor in actors],
        "business_rules": [rule.model_dump() for rule in business_rules],
        "use_case_definitions": [
            use_case.model_dump() for use_case in use_case_definitions
        ],
        "architecture": architecture.model_dump(),
        "data_model": data_model.model_dump(),
    }
