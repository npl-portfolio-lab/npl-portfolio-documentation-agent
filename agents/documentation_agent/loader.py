from pathlib import Path

import yaml

from .models import (
    FunctionalRequirement,
    Actor,
    BusinessRule,
    UseCaseDefinition,
)


def load_functional_requirements(
    file_path: Path,
) -> list[FunctionalRequirement]:

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
