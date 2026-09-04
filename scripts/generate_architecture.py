from pathlib import Path

from agents.documentation_agent.architecture_renderer import (
    ArchitectureRenderer,
)
from agents.documentation_agent.context_builder import (
    build_documentation_context,
)


OUTPUT_FILE = Path(
    "docs/architecture/system_architecture.md"
)


def main() -> None:
    """
    Genera automáticamente la documentación
    de arquitectura del proyecto.
    """
    context = build_documentation_context()

    renderer = ArchitectureRenderer(
        context
    )

    markdown = renderer.render()

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        markdown,
        encoding="utf-8",
    )

    print(
        "DOCUMENTACIÓN DE ARQUITECTURA GENERADA"
    )

    print(
        f"Archivo: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
