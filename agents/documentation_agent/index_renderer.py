from pathlib import Path

from .context_builder import build_documentation_context


class UseCaseIndexRenderer:

    def __init__(
        self,
        output_path: Path = Path(
            "docs/use_cases/README.md"
        ),
    ):
        self.output_path = output_path

    def render(self) -> Path:

        context = build_documentation_context()

        requirements = context[
            "functional_requirements"
        ]

        lines = [
            "# Índice de Casos de Uso",
            "",
            (
                "Este documento contiene la relación "
                "entre los requerimientos funcionales "
                "y los casos de uso del proyecto."
            ),
            "",
            "## Casos de uso",
            "",
        ]

        for requirement in requirements:

            requirement_number = (
                requirement["id"].split("-")[1]
            )

            use_case_id = (
                f"CU-{requirement_number}"
            )

            lines.append(
                (
                    f"- [{use_case_id} - "
                    f'{requirement["name"]}]'
                    f"({use_case_id}.md)"
                )
            )

        content = "\n".join(lines)

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.output_path.write_text(
            content,
            encoding="utf-8",
        )

        return self.output_path
