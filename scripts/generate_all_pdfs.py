from pathlib import Path

from agents.documentation_agent.agent import (
    DocumentationAgent,
)
from agents.documentation_agent.loader import (
    load_functional_requirements,
)
from agents.documentation_agent.pdf_renderer import (
    PDFRenderer,
)
from tests.fake_llm_client import (
    FakeLLMClient,
)


def main() -> None:

    requirements_path = Path(
        "requirements/"
        "functional_requirements.yaml"
    )

    requirements = (
        load_functional_requirements(
            requirements_path
        )
    )

    llm_client = FakeLLMClient()

    agent = DocumentationAgent(
        llm_client=llm_client
    )

    renderer = PDFRenderer()

    print()
    print(
        "Generando documentos PDF..."
    )
    print()

    for requirement in requirements:

        print(
            f"Procesando "
            f"{requirement.id} - "
            f"{requirement.name}"
        )

        use_case = (
            agent.generate_use_case(
                requirement.id
            )
        )

        output_path = (
            renderer.render_use_case(
                use_case
            )
        )

        print(
            f"  -> Generado: "
            f"{output_path}"
        )

    print()
    print(
        "Generación PDF finalizada "
        "correctamente."
    )


if __name__ == "__main__":
    main()
