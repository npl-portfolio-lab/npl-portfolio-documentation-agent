from agents.documentation_agent.context_builder import (
    build_documentation_context,
)


def main() -> None:

    context = build_documentation_context()

    requirements = {
        item["id"]: item
        for item in context["functional_requirements"]
    }

    actors = {
        item["id"]: item
        for item in context["actors"]
    }

    business_rules = {
        item["id"]: item
        for item in context["business_rules"]
    }

    use_case_definitions = context[
        "use_case_definitions"
    ]

    errors = []

    print()
    print("VALIDANDO TRAZABILIDAD DE CASOS DE USO")
    print("=" * 50)
    print()

    for use_case in use_case_definitions:

        use_case_id = use_case["id"]
        requirement_id = use_case[
            "related_requirement"
        ]
        actor_id = use_case[
            "primary_actor"
        ]

        print(
            f"{use_case_id} -> "
            f"{requirement_id} -> "
            f"{actor_id}"
        )

        # Validar requerimiento
        if requirement_id not in requirements:
            errors.append(
                f"{use_case_id}: "
                f"requerimiento inexistente "
                f"{requirement_id}"
            )

        # Validar actor
        if actor_id not in actors:
            errors.append(
                f"{use_case_id}: "
                f"actor inexistente "
                f"{actor_id}"
            )

        # Validar reglas de negocio
        for rule_id in use_case[
            "business_rules"
        ]:

            if rule_id not in business_rules:
                errors.append(
                    f"{use_case_id}: "
                    f"regla de negocio inexistente "
                    f"{rule_id}"
                )

        # Validar correspondencia CU-XXX / RF-XXX
        expected_requirement_id = (
            use_case_id.replace(
                "CU-",
                "RF-",
            )
        )

        if (
            requirement_id
            != expected_requirement_id
        ):
            errors.append(
                f"{use_case_id}: "
                f"debería estar relacionado con "
                f"{expected_requirement_id}, "
                f"pero está relacionado con "
                f"{requirement_id}"
            )

    print()
    print("=" * 50)

    if errors:

        print(
            "SE ENCONTRARON ERRORES:"
        )

        print()

        for error in errors:
            print(
                f"- {error}"
            )

        raise SystemExit(1)

    print(
        "TRAZABILIDAD VALIDADA CORRECTAMENTE"
    )

    print(
        f"Casos de uso validados: "
        f"{len(use_case_definitions)}"
    )


if __name__ == "__main__":
    main()
