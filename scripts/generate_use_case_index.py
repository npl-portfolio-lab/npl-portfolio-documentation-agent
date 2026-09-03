from agents.documentation_agent.index_renderer import (
    UseCaseIndexRenderer,
)


def main():

    renderer = UseCaseIndexRenderer()

    output_path = renderer.render()

    print(
        f"Índice generado correctamente: "
        f"{output_path}"
    )


if __name__ == "__main__":
    main()
