from pathlib import Path

from agents.documentation_agent.loader import (
    load_architecture,
    load_data_model,
)


BASE_DIR = Path(__file__).resolve().parent.parent

ARCHITECTURE_FILE = BASE_DIR / "requirements" / "architecture.yaml"
DATA_MODEL_FILE = BASE_DIR / "requirements" / "data_model.yaml"


def main() -> None:
    architecture = load_architecture(ARCHITECTURE_FILE)
    data_model = load_data_model(DATA_MODEL_FILE)

    print("ARQUITECTURA")
    print("-" * 50)

    for component in architecture.components:
        print(f"{component.id} -> {component.name}")

    print()

    print("MODELO DE DATOS")
    print("-" * 50)

    for entity in data_model.entities:
        print(f"{entity.id} -> {entity.name}")

    print()

    print("VALIDACIÓN COMPLETADA")
    print(f"Componentes: {len(architecture.components)}")
    print(f"Entidades: {len(data_model.entities)}")


if __name__ == "__main__":
    main()
