from pathlib import Path

from agents.documentation_agent.loader import (
    load_functional_requirements,
)


def main():

    requirements_path = Path(
        "requirements/functional_requirements.yaml"
    )

    use_cases_directory = Path(
        "docs/use_cases"
    )

    requirements = load_functional_requirements(
        requirements_path
    )

    total_requirements = len(requirements)

    covered_requirements = 0

    missing_use_cases = []

    print(
        "\nValidando cobertura documental...\n"
    )

    for requirement in requirements:

        requirement_number = (
            requirement.id.split("-")[1]
        )

        use_case_id = (
            f"CU-{requirement_number}"
        )

        use_case_path = (
            use_cases_directory
            / f"{use_case_id}.md"
        )

        if use_case_path.exists():

            covered_requirements += 1

            print(
                f"{requirement.id} "
                f"-> {use_case_id} "
                f"-> OK"
            )

        else:

            missing_use_cases.append(
                (
                    requirement.id,
                    use_case_id,
                )
            )

            print(
                f"{requirement.id} "
                f"-> {use_case_id} "
                f"-> FALTANTE"
            )

    print("\nResumen")
    print("-------")

    print(
        f"Requerimientos totales: "
        f"{total_requirements}"
    )

    print(
        f"Casos de uso encontrados: "
        f"{covered_requirements}"
    )

    print(
        f"Sin cobertura: "
        f"{len(missing_use_cases)}"
    )

    if missing_use_cases:

        print(
            "\nFASE 1: COBERTURA INCOMPLETA"
        )

        print(
            "\nCasos de uso faltantes:"
        )

        for requirement_id, use_case_id in missing_use_cases:

            print(
                f"- {requirement_id} "
                f"requiere {use_case_id}"
            )

        raise SystemExit(1)

    print(
        "\nFASE 1: COBERTURA VALIDADA"
    )


if __name__ == "__main__":
    main()
