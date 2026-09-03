from pathlib import Path

from agents.documentation_agent.loader import (
    load_business_rules,
)


path = Path(
    "requirements/business_rules.yaml"
)

rules = load_business_rules(path)

for rule in rules:
    print(
        rule.id,
        "-",
        rule.name,
        "-",
        rule.category,
        "-",
        rule.priority,
    )
