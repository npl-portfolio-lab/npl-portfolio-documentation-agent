from pathlib import Path

from agents.documentation_agent.pdf_renderer import PDFRenderer


def find_markdown_files(
    docs_directory: Path,
) -> list[Path]:
    """
    Busca todos los archivos Markdown existentes
    dentro del directorio docs/.

    La búsqueda es recursiva, por lo que también
    encuentra archivos ubicados en subdirectorios:

        docs/use_cases/
        docs/architecture/
        docs/data/
        docs/machine_learning/
        docs/etl/
        etc.

    Los archivos README.md se excluyen porque
    normalmente funcionan como índices de navegación
    del repositorio y no como documentos finales.
    """

    markdown_files = []

    # rglob("*.md") busca recursivamente todos
    # los archivos Markdown dentro de docs/.
    for markdown_path in docs_directory.rglob("*.md"):

        # No generamos PDF para README.md.
        if markdown_path.name.lower() == "readme.md":
            continue

        markdown_files.append(
            markdown_path
        )

    # Ordenamos para que la generación siempre
    # tenga un orden predecible.
    return sorted(markdown_files)


def main() -> None:
    """
    Convierte automáticamente a PDF todos los
    documentos Markdown existentes dentro de docs/.

    Este script NO genera el contenido documental.

    Por ejemplo:

        DocumentationAgent
            -> genera CU-001.md

        ArchitectureRenderer
            -> genera system_architecture.md

        DataModelRenderer
            -> genera data_model.md

    Este script toma esos Markdown ya generados
    y produce sus respectivas versiones PDF.
    """

    # -------------------------------------------------
    # 1. Determinar la raíz del proyecto
    # -------------------------------------------------
    #
    # __file__ apunta a:
    #
    # scripts/generate_all_pdfs.py
    #
    # parents[1] nos lleva a:
    #
    # npl-portfolio-ml/
    #
    project_root = (
        Path(__file__)
        .resolve()
        .parents[1]
    )

    # Directorio principal de documentación.
    docs_directory = (
        project_root
        / "docs"
    )

    # -------------------------------------------------
    # 2. Verificar que docs/ exista
    # -------------------------------------------------

    if not docs_directory.exists():
        print()
        print(
            "ERROR: No existe el directorio docs/."
        )
        print(
            f"Ruta esperada: {docs_directory}"
        )
        return

    # -------------------------------------------------
    # 3. Buscar todos los Markdown
    # -------------------------------------------------

    markdown_files = find_markdown_files(
        docs_directory
    )

    if not markdown_files:
        print()
        print(
            "No se encontraron documentos Markdown "
            "para convertir."
        )
        return

    # -------------------------------------------------
    # 4. Crear el renderer PDF
    # -------------------------------------------------

    renderer = PDFRenderer()

    print()
    print(
        "GENERACIÓN GENERAL DE DOCUMENTOS PDF"
    )
    print(
        "=" * 50
    )
    print()

    print(
        f"Documentos encontrados: "
        f"{len(markdown_files)}"
    )
    print()

    generated_count = 0
    error_count = 0

    # -------------------------------------------------
    # 5. Convertir cada Markdown a PDF
    # -------------------------------------------------

    for markdown_path in markdown_files:

        # Ruta relativa solamente para mostrar
        # mensajes más limpios en la terminal.
        relative_path = (
            markdown_path.relative_to(
                project_root
            )
        )

        print(
            f"Procesando: {relative_path}"
        )

        try:
            # Este será el método genérico que
            # agregaremos a PDFRenderer.
            #
            # Recibe cualquier archivo .md,
            # independientemente del tipo de documento.
            output_path = (
                renderer.render_markdown_file(
                    markdown_path
                )
            )

            relative_output = (
                output_path.relative_to(
                    project_root
                )
            )

            print(
                f"  -> Generado: "
                f"{relative_output}"
            )

            generated_count += 1

        except Exception as error:
            # Un error en un documento no debe
            # detener la generación de todos
            # los documentos restantes.
            print(
                f"  -> ERROR: {error}"
            )

            error_count += 1

        print()

    # -------------------------------------------------
    # 6. Resumen final
    # -------------------------------------------------

    print(
        "=" * 50
    )

    print(
        "GENERACIÓN PDF FINALIZADA"
    )

    print(
        f"PDF generados: {generated_count}"
    )

    print(
        f"Errores: {error_count}"
    )

    print()


if __name__ == "__main__":
    main()