from pathlib import Path

from agents.documentation_agent.loader import (
    load_functional_requirements,
)


path = Path(
    "requirements/functional_requirements.yaml"
)

requirements = load_functional_requirements(path)

for requirement in requirements:
    print(
        requirement.id,
        "-",
        requirement.name,
    )
