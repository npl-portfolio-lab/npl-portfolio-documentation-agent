from .models import UseCase


def validate_use_case_references(
    use_case: UseCase,
    context: dict,
) -> None:

    valid_actor_ids = {actor["id"] for actor in context["actors"]}

    valid_requirement_ids = {
        requirement["id"] for requirement in context["functional_requirements"]
    }

    valid_business_rule_ids = {rule["id"] for rule in context["business_rules"]}

    if use_case.primary_actor not in valid_actor_ids:
        raise ValueError(f"Invalid actor reference: " f"{use_case.primary_actor}")

    for requirement_id in use_case.related_requirements:
        if requirement_id not in valid_requirement_ids:
            raise ValueError(f"Invalid requirement reference: " f"{requirement_id}")

    for rule_id in use_case.business_rules:
        if rule_id not in valid_business_rule_ids:
            raise ValueError(f"Invalid business rule reference: " f"{rule_id}")
