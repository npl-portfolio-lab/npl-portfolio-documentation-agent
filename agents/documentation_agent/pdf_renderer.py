from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    ParagraphStyle,
    getSampleStyleSheet,
)
from reportlab.lib.units import cm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from .context_builder import (
    build_documentation_context,
)
from .models import UseCase


class PDFRenderer:
    """
    Renderizador PDF general del proyecto.

    Mantiene compatibilidad con la generación
    específica de casos de uso mediante:

        render_use_case()

    y además permite convertir cualquier archivo
    Markdown mediante:

        render_markdown_file()

    De esta manera el mismo renderer puede utilizarse
    para:

        - Casos de uso
        - Arquitectura
        - Modelo de datos
        - ETL
        - Machine Learning
        - Backtesting
        - Valoración financiera
        - API
        - Observabilidad
        - Documentación futura
    """

    def __init__(
        self,
        output_directory: Path = Path("docs/use_cases"),
    ):
        """
        Inicializa el renderer.

        output_directory se mantiene principalmente
        por compatibilidad con render_use_case().

        Para render_markdown_file() el PDF se crea
        automáticamente en la misma carpeta donde
        se encuentra el Markdown.
        """

        self.output_directory = output_directory

        self.styles = getSampleStyleSheet()

        self._configure_styles()

    # =================================================
    # CONFIGURACIÓN DE ESTILOS
    # =================================================

    def _configure_styles(
        self,
    ) -> None:
        """
        Configura los estilos utilizados tanto para
        casos de uso como para Markdown genérico.
        """

        # -------------------------------------------------
        # Título principal
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="UseCaseTitle",
                parent=self.styles["Title"],
                alignment=TA_CENTER,
                fontSize=18,
                leading=22,
                spaceAfter=16,
            )
        )

        # -------------------------------------------------
        # Título general para documentos Markdown
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="DocumentTitle",
                parent=self.styles["Title"],
                alignment=TA_CENTER,
                fontSize=18,
                leading=22,
                spaceAfter=18,
                textColor=colors.HexColor("#1F4E78"),
            )
        )

        # -------------------------------------------------
        # Encabezado nivel 2
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="SectionTitle",
                parent=self.styles["Heading2"],
                fontSize=13,
                leading=16,
                spaceBefore=10,
                spaceAfter=8,
                textColor=colors.HexColor("#1F4E78"),
            )
        )

        # -------------------------------------------------
        # Encabezado nivel 3
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="SubsectionTitle",
                parent=self.styles["Heading3"],
                fontSize=11,
                leading=14,
                spaceBefore=8,
                spaceAfter=6,
                textColor=colors.HexColor("#365F91"),
            )
        )

        # -------------------------------------------------
        # Texto normal
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="BodyCustom",
                parent=self.styles["BodyText"],
                fontSize=10,
                leading=15,
                spaceAfter=6,
            )
        )

        # -------------------------------------------------
        # Metadatos
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="Metadata",
                parent=self.styles["BodyText"],
                fontSize=10,
                leading=14,
                spaceAfter=4,
            )
        )

        # -------------------------------------------------
        # Código / texto monoespaciado
        # -------------------------------------------------

        self.styles.add(
            ParagraphStyle(
                name="CodeBlock",
                parent=self.styles["Code"],
                fontName="Courier",
                fontSize=8,
                leading=11,
                leftIndent=10,
                rightIndent=10,
                spaceBefore=6,
                spaceAfter=8,
                backColor=colors.HexColor("#F4F4F4"),
                borderColor=colors.HexColor("#D0D0D0"),
                borderWidth=0.5,
                borderPadding=6,
            )
        )

    # =================================================
    # CASOS DE USO
    # =================================================

    def render_use_case(
        self,
        use_case: UseCase,
    ) -> Path:
        """
        Genera el PDF de un caso de uso.

        Este método se conserva para evitar romper
        el comportamiento existente del proyecto.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = self.output_directory / f"{use_case.id}.pdf"

        document = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=2 * cm,
            leftMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm,
            title=(f"{use_case.id} - " f"{use_case.name}"),
            author=("NPL Portfolio " "Documentation Agent"),
        )

        story = self._build_content(use_case)

        document.build(story)

        return output_path

    def _build_content(
        self,
        use_case: UseCase,
    ) -> list:
        """
        Construye el contenido del PDF
        específico para casos de uso.
        """

        context = build_documentation_context()

        actor_name = self._get_actor_name(
            use_case.primary_actor,
            context,
        )

        requirement_labels = [
            self._get_requirement_label(
                requirement_id,
                context,
            )
            for requirement_id in use_case.related_requirements
        ]

        business_rule_labels = [
            self._get_business_rule_label(
                rule_id,
                context,
            )
            for rule_id in use_case.business_rules
        ]

        story = []

        story.append(
            Paragraph(
                (f"{use_case.id} - " f"{use_case.name}"),
                self.styles["UseCaseTitle"],
            )
        )

        story.append(
            Paragraph(
                "Información general",
                self.styles["SectionTitle"],
            )
        )

        story.append(
            Paragraph(
                ("<b>Identificador:</b> " f"{use_case.id}"),
                self.styles["Metadata"],
            )
        )

        story.append(
            Paragraph(
                (
                    "<b>Actor principal:</b> "
                    f"{use_case.primary_actor} "
                    f"- {actor_name}"
                ),
                self.styles["Metadata"],
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

        self._add_text_section(
            story,
            "Objetivo",
            use_case.objective,
        )

        self._add_bullet_section(
            story,
            "Precondiciones",
            use_case.preconditions,
        )

        self._add_numbered_section(
            story,
            "Flujo principal",
            use_case.main_flow,
        )

        self._add_bullet_section(
            story,
            "Flujos alternativos",
            use_case.alternative_flows,
        )

        self._add_bullet_section(
            story,
            "Postcondiciones",
            use_case.postconditions,
        )

        self._add_bullet_section(
            story,
            "Requerimientos relacionados",
            requirement_labels,
        )

        self._add_bullet_section(
            story,
            "Reglas de negocio",
            business_rule_labels,
        )

        return story

    # =================================================
    # MARKDOWN GENÉRICO
    # =================================================

    def render_markdown_file(
        self,
        markdown_path: Path,
    ) -> Path:
        """
        Convierte cualquier archivo Markdown
        del proyecto a PDF.

        Ejemplo:

            docs/data/data_model.md

        genera:

            docs/data/data_model.pdf

        El PDF se crea en la misma carpeta
        del Markdown original.
        """

        markdown_path = Path(markdown_path)

        # -------------------------------------------------
        # Validaciones básicas
        # -------------------------------------------------

        if not markdown_path.exists():
            raise FileNotFoundError(
                "No existe el archivo Markdown: " f"{markdown_path}"
            )

        if markdown_path.suffix.lower() != ".md":
            raise ValueError("El archivo debe tener extensión .md: " f"{markdown_path}")

        # -------------------------------------------------
        # Leer Markdown
        # -------------------------------------------------

        markdown_text = markdown_path.read_text(encoding="utf-8")

        # -------------------------------------------------
        # El PDF tendrá el mismo nombre
        # -------------------------------------------------

        output_path = markdown_path.with_suffix(".pdf")

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # -------------------------------------------------
        # Obtener título
        # -------------------------------------------------

        document_title = self._extract_document_title(
            markdown_text,
            markdown_path,
        )

        # -------------------------------------------------
        # Crear documento PDF
        # -------------------------------------------------

        document = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=1.7 * cm,
            leftMargin=1.7 * cm,
            topMargin=1.8 * cm,
            bottomMargin=1.8 * cm,
            title=document_title,
            author=("NPL Portfolio " "Documentation Agent"),
        )

        # -------------------------------------------------
        # Convertir Markdown a elementos ReportLab
        # -------------------------------------------------

        story = self._markdown_to_story(markdown_text)

        document.build(story)

        return output_path

    def _extract_document_title(
        self,
        markdown_text: str,
        markdown_path: Path,
    ) -> str:
        """
        Obtiene el título del documento.

        Primero intenta encontrar un encabezado Markdown:

            # Modelo Lógico de Datos

        Si no existe, utiliza el nombre del archivo.
        """

        for line in markdown_text.splitlines():

            stripped = line.strip()

            if stripped.startswith("# "):
                return stripped[2:].strip()

        # Ejemplo:
        #
        # data_model
        #
        # se convierte en:
        #
        # Data Model
        #

        return markdown_path.stem.replace("_", " ").replace("-", " ").title()

    def _markdown_to_story(
        self,
        markdown_text: str,
    ) -> list:
        """
        Convierte Markdown sencillo a componentes
        de ReportLab.

        Actualmente soporta:

            # Título
            ## Sección
            ### Subsección
            texto normal
            listas con -
            listas con *
            listas numeradas
            tablas Markdown
            bloques ```code```
            texto en negrita
            texto en cursiva

        También detecta bloques Mermaid.
        Como ReportLab no interpreta Mermaid,
        estos se muestran como bloque de código
        en el PDF.
        """

        story = []

        lines = markdown_text.splitlines()

        index = 0

        first_h1_rendered = False

        while index < len(lines):

            line = lines[index]
            stripped = line.strip()

            # -------------------------------------------------
            # Línea vacía
            # -------------------------------------------------

            if not stripped:
                index += 1
                continue

            # -------------------------------------------------
            # Bloque de código
            # -------------------------------------------------

            if stripped.startswith("```"):
                language = stripped[3:].strip()

                code_lines = []

                index += 1

                while index < len(lines) and not lines[index].strip().startswith("```"):
                    code_lines.append(lines[index])

                    index += 1

                # Saltar ```
                if index < len(lines):
                    index += 1

                code_text = "\n".join(code_lines)

                # Mermaid se conserva como texto.
                # Así no se pierde el diagrama lógico
                # aunque todavía no se renderice
                # gráficamente dentro del PDF.
                if language:
                    code_text = f"[{language}]\n" f"{code_text}"

                story.append(
                    Paragraph(
                        self._format_code(code_text),
                        self.styles["CodeBlock"],
                    )
                )

                continue

            # -------------------------------------------------
            # Tabla Markdown
            # -------------------------------------------------

            if self._is_table_start(
                lines,
                index,
            ):
                table_lines = []

                while index < len(lines) and "|" in lines[index]:
                    table_lines.append(lines[index])

                    index += 1

                table = self._build_markdown_table(table_lines)

                if table is not None:
                    story.append(table)

                    story.append(
                        Spacer(
                            1,
                            10,
                        )
                    )

                continue

            # -------------------------------------------------
            # H1
            # -------------------------------------------------

            if stripped.startswith("# "):
                title = stripped[2:].strip()

                style_name = (
                    "DocumentTitle" if not first_h1_rendered else "SectionTitle"
                )

                story.append(
                    Paragraph(
                        self._format_inline_markdown(title),
                        self.styles[style_name],
                    )
                )

                first_h1_rendered = True

                index += 1
                continue

            # -------------------------------------------------
            # H2
            # -------------------------------------------------

            if stripped.startswith("## "):
                story.append(
                    Paragraph(
                        self._format_inline_markdown(stripped[3:].strip()),
                        self.styles["SectionTitle"],
                    )
                )

                index += 1
                continue

            # -------------------------------------------------
            # H3 o encabezados inferiores
            # -------------------------------------------------

            if stripped.startswith("### "):
                title = stripped.lstrip("#").strip()

                story.append(
                    Paragraph(
                        self._format_inline_markdown(title),
                        self.styles["SubsectionTitle"],
                    )
                )

                index += 1
                continue

            # -------------------------------------------------
            # Lista con viñetas
            # -------------------------------------------------

            if stripped.startswith("- ") or stripped.startswith("* "):
                items = []

                while index < len(lines):

                    current = lines[index].strip()

                    if not (current.startswith("- ") or current.startswith("* ")):
                        break

                    items.append(current[2:].strip())

                    index += 1

                self._append_generic_list(
                    story,
                    items,
                    numbered=False,
                )

                continue

            # -------------------------------------------------
            # Lista numerada
            # -------------------------------------------------

            if re.match(
                r"^\d+\.\s+",
                stripped,
            ):
                items = []

                while index < len(lines):

                    current = lines[index].strip()

                    match = re.match(
                        r"^\d+\.\s+(.*)",
                        current,
                    )

                    if not match:
                        break

                    items.append(match.group(1))

                    index += 1

                self._append_generic_list(
                    story,
                    items,
                    numbered=True,
                )

                continue

            # -------------------------------------------------
            # Texto normal
            # -------------------------------------------------

            paragraph_lines = [stripped]

            index += 1

            while index < len(lines):

                next_line = lines[index].strip()

                if not next_line:
                    break

                if (
                    next_line.startswith("#")
                    or next_line.startswith("- ")
                    or next_line.startswith("* ")
                    or next_line.startswith("```")
                    or re.match(
                        r"^\d+\.\s+",
                        next_line,
                    )
                ):
                    break

                if self._is_table_start(
                    lines,
                    index,
                ):
                    break

                paragraph_lines.append(next_line)

                index += 1

            paragraph_text = " ".join(paragraph_lines)

            story.append(
                Paragraph(
                    self._format_inline_markdown(paragraph_text),
                    self.styles["BodyCustom"],
                )
            )

        return story

    # =================================================
    # TABLAS MARKDOWN
    # =================================================

    def _is_table_start(
        self,
        lines: list[str],
        index: int,
    ) -> bool:
        """
        Detecta tablas Markdown.

        Ejemplo:

        | Campo | Tipo |
        | --- | --- |
        | id | UUID |
        """

        if index + 1 >= len(lines):
            return False

        current = lines[index].strip()

        next_line = lines[index + 1].strip()

        if "|" not in current or "|" not in next_line:
            return False

        separator_pattern = r"^\s*\|?" r"\s*:?-+:?\s*" r"(\|\s*:?-+:?\s*)+" r"\|?\s*$"

        return bool(
            re.match(
                separator_pattern,
                next_line,
            )
        )

    def _build_markdown_table(
        self,
        table_lines: list[str],
    ):
        """
        Convierte una tabla Markdown en
        una tabla de ReportLab.
        """

        if len(table_lines) < 2:
            return None

        rows = []

        for line_index, line in enumerate(table_lines):

            # La segunda fila es el separador:
            #
            # | --- | --- |
            #
            # por tanto no se incluye.
            if line_index == 1:
                continue

            clean_line = line.strip().strip("|")

            cells = [cell.strip() for cell in clean_line.split("|")]

            row = [
                Paragraph(
                    self._format_inline_markdown(cell),
                    self.styles["BodyCustom"],
                )
                for cell in cells
            ]

            rows.append(row)

        if not rows:
            return None

        number_of_columns = len(rows[0])

        # A4 dispone aproximadamente de
        # 17 cm útiles con nuestros márgenes.
        available_width = 17.0 * cm

        column_width = available_width / number_of_columns

        table = Table(
            rows,
            colWidths=[column_width for _ in range(number_of_columns)],
            repeatRows=1,
        )

        table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#D9EAF7"),
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#1F1F1F"),
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold",
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.HexColor("#B8B8B8"),
                    ),
                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "TOP",
                    ),
                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        5,
                    ),
                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        5,
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        5,
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        5,
                    ),
                ]
            )
        )

        return table

    # =================================================
    # LISTAS GENÉRICAS
    # =================================================

    def _append_generic_list(
        self,
        story: list,
        items: list[str],
        numbered: bool,
    ) -> None:
        """
        Agrega una lista Markdown al documento.
        """

        if not items:
            return

        list_items = [
            ListItem(
                Paragraph(
                    self._format_inline_markdown(item),
                    self.styles["BodyCustom"],
                )
            )
            for item in items
        ]

        story.append(
            ListFlowable(
                list_items,
                bulletType=("1" if numbered else "bullet"),
                start=("1" if numbered else None),
                leftIndent=(22 if numbered else 18),
            )
        )

        story.append(
            Spacer(
                1,
                5,
            )
        )

    # =================================================
    # FORMATO MARKDOWN
    # =================================================

    def _format_inline_markdown(
        self,
        text: str,
    ) -> str:
        """
        Convierte parte del Markdown inline
        al formato compatible con Paragraph
        de ReportLab.

        Soporta:

            **negrita**
            *cursiva*
            `codigo`
        """

        # Escapar primero caracteres especiales
        # para evitar que ReportLab interprete
        # HTML accidental.
        text = html.escape(text)

        # Código inline.
        text = re.sub(
            r"`([^`]+)`",
            r'<font name="Courier">\1</font>',
            text,
        )

        # Negrita.
        text = re.sub(
            r"\*\*(.+?)\*\*",
            r"<b>\1</b>",
            text,
        )

        # Cursiva.
        text = re.sub(
            r"(?<!\*)\*([^*]+)\*(?!\*)",
            r"<i>\1</i>",
            text,
        )

        return text

    def _format_code(
        self,
        text: str,
    ) -> str:
        """
        Prepara un bloque de código para que
        ReportLab preserve saltos de línea.
        """

        escaped = html.escape(text)

        return escaped.replace(
            "\n",
            "<br/>",
        )

    # =================================================
    # MÉTODOS EXISTENTES PARA CASOS DE USO
    # =================================================

    def _add_text_section(
        self,
        story: list,
        title: str,
        text: str,
    ) -> None:

        story.append(
            Paragraph(
                title,
                self.styles["SectionTitle"],
            )
        )

        story.append(
            Paragraph(
                text.strip(),
                self.styles["BodyCustom"],
            )
        )

    def _add_bullet_section(
        self,
        story: list,
        title: str,
        items: list[str],
    ) -> None:

        story.append(
            Paragraph(
                title,
                self.styles["SectionTitle"],
            )
        )

        if not items:

            story.append(
                Paragraph(
                    "No definido.",
                    self.styles["BodyCustom"],
                )
            )

            return

        list_items = [
            ListItem(
                Paragraph(
                    item,
                    self.styles["BodyCustom"],
                )
            )
            for item in items
        ]

        story.append(
            ListFlowable(
                list_items,
                bulletType="bullet",
                leftIndent=18,
            )
        )

    def _add_numbered_section(
        self,
        story: list,
        title: str,
        items: list[str],
    ) -> None:

        story.append(
            Paragraph(
                title,
                self.styles["SectionTitle"],
            )
        )

        if not items:

            story.append(
                Paragraph(
                    "No definido.",
                    self.styles["BodyCustom"],
                )
            )

            return

        list_items = [
            ListItem(
                Paragraph(
                    item,
                    self.styles["BodyCustom"],
                )
            )
            for item in items
        ]

        story.append(
            ListFlowable(
                list_items,
                bulletType="1",
                start="1",
                leftIndent=22,
            )
        )

    def _get_actor_name(
        self,
        actor_id: str,
        context: dict,
    ) -> str:

        for actor in context["actors"]:

            if actor["id"] == actor_id:
                return actor["name"]

        return "Actor no encontrado"

    def _get_requirement_label(
        self,
        requirement_id: str,
        context: dict,
    ) -> str:

        for requirement in context["functional_requirements"]:

            if requirement["id"] == requirement_id:
                return f'{requirement["id"]} - ' f'{requirement["name"]}'

        return requirement_id

    def _get_business_rule_label(
        self,
        rule_id: str,
        context: dict,
    ) -> str:

        for rule in context["business_rules"]:

            if rule["id"] == rule_id:
                return f'{rule["id"]} - ' f'{rule["name"]}'

        return rule_id
