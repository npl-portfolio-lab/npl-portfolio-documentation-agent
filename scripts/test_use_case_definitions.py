from pathlib import Path

from agents.documentation_agent.loader import (
    load_use_case_definitions,
)


path = Path(
    "requirements/use_case_definitions.yaml"
)

use_cases = load_use_case_definitions(
    path
)

for use_case in use_cases:
    print(
        use_case.id,
        "-",
        use_case.name,
        "-",
        use_case.related_requirement,
        "-",
        use_case.primary_actor,
    )
