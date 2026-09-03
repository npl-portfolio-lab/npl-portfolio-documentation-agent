from pathlib import Path

from agents.documentation_agent.agent import (
    DocumentationAgent,
)
from agents.documentation_agent.loader import (
    load_functional_requirements,
)
from agents.documentation_agent.markdown_renderer import (
    MarkdownRenderer,
)
from tests.fake_llm_client import (
    FakeLLMClient,
)


def main():

    requirements_path = Path(
        "requirements/functional_requirements.yaml"
    )

    requirements = load_functional_requirements(
        requirements_path
    )

    client = FakeLLMClient()

    agent = DocumentationAgent(
        llm_client=client,
    )

    renderer = MarkdownRenderer()

    print(
        "\nGenerando casos de uso...\n"
    )

    for requirement in requirements:

        print(
            f"Procesando {requirement.id} "
            f"- {requirement.name}"
        )

        use_case = agent.generate_use_case(
            requirement.id
        )

        output_path = renderer.render_use_case(
            use_case
        )

        print(
            f"  -> Generado: {output_path}"
        )

    print(
        "\nGeneración finalizada correctamente."
    )


if __name__ == "__main__":
    main()
