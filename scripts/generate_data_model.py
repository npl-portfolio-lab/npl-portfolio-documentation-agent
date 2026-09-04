from pathlib import Path

from agents.documentation_agent.context_builder import (
    build_documentation_context,
)
from agents.documentation_agent.data_model_renderer import (
    DataModelRenderer,
)


def main() -> None:
    """
    Genera la documentación Markdown del modelo lógico
    de datos a partir de las fuentes YAML del proyecto.
    """

    context = build_documentation_context()

    renderer = DataModelRenderer(context)

    markdown = renderer.render()

    output_path = Path(
        "docs/data/data_model.md"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        markdown,
        encoding="utf-8",
    )

    print(
        "DOCUMENTACIÓN DEL MODELO DE DATOS GENERADA"
    )
    print(
        f"Archivo: {output_path}"
    )


if __name__ == "__main__":
    main()