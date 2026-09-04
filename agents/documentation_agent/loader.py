from pathlib import Path

import yaml

from .models import (
    FunctionalRequirement,
    Actor,
    BusinessRule,
    UseCaseDefinition,
    ArchitectureDefinition,
    DataModelDefinition,
)


def load_functional_requirements(
    file_path: Path,
) -> list[FunctionalRequirement]:
    """
    Carga y valida los requerimientos funcionales
    definidos en un archivo YAML.
    """
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    requirements = data.get(
        "functional_requirements",
        [],
    )

    return [FunctionalRequirement(**requirement) for requirement in requirements]


def load_actors(
    file_path: Path,
) -> list[Actor]:
    """
    Carga y valida los actores definidos
    para los casos de uso del sistema.
    """
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    actors = data.get(
        "actors",
        [],
    )

    return [Actor(**actor) for actor in actors]


def load_business_rules(
    file_path: Path,
) -> list[BusinessRule]:
    """
    Carga y valida las reglas de negocio
    definidas para el proyecto.
    """
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    rules = data.get(
        "business_rules",
        [],
    )

    return [BusinessRule(**rule) for rule in rules]


def load_use_case_definitions(
    file_path: Path,
) -> list[UseCaseDefinition]:
    """
    Carga y valida las definiciones estructuradas
    de los casos de uso.
    """
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    use_cases = data.get(
        "use_cases",
        [],
    )

    return [UseCaseDefinition(**use_case) for use_case in use_cases]


def load_architecture(
    file_path: Path,
) -> ArchitectureDefinition:
    """
    Carga y valida la definición estructurada
    de la arquitectura del sistema.
    """
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    architecture = data.get(
        "architecture",
        {},
    )

    return ArchitectureDefinition(**architecture)


def load_data_model(
    file_path: Path,
) -> DataModelDefinition:
    """
    Carga y valida la definición estructurada
    del modelo lógico de datos.
    """
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file)

    data_model = data.get(
        "data_model",
        {},
    )

    return DataModelDefinition(**data_model)
