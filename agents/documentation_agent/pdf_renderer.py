from pathlib import Path

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
)

from .context_builder import (
    build_documentation_context,
)
from .models import UseCase


class PDFRenderer:

    def __init__(
        self,
        output_directory: Path = Path(
            "docs/use_cases"
        ),
    ):
        self.output_directory = (
            output_directory
        )

        self.styles = (
            getSampleStyleSheet()
        )

        self._configure_styles()

    def _configure_styles(
        self,
    ) -> None:

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

        self.styles.add(
            ParagraphStyle(
                name="SectionTitle",
                parent=self.styles[
                    "Heading2"
                ],
                fontSize=13,
                leading=16,
                spaceBefore=10,
                spaceAfter=8,
                textColor=colors.HexColor(
                    "#1F4E78"
                ),
            )
        )

        self.styles.add(
            ParagraphStyle(
                name="BodyCustom",
                parent=self.styles[
                    "BodyText"
                ],
                fontSize=10,
                leading=15,
                spaceAfter=6,
            )
        )

        self.styles.add(
            ParagraphStyle(
                name="Metadata",
                parent=self.styles[
                    "BodyText"
                ],
                fontSize=10,
                leading=14,
                spaceAfter=4,
            )
        )

    def render_use_case(
        self,
        use_case: UseCase,
    ) -> Path:

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = (
            self.output_directory
            / f"{use_case.id}.pdf"
        )

        document = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=2 * cm,
            leftMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm,
            title=(
                f"{use_case.id} - "
                f"{use_case.name}"
            ),
            author=(
                "NPL Portfolio "
                "Documentation Agent"
            ),
        )

        story = (
            self._build_content(
                use_case
            )
        )

        document.build(
            story
        )

        return output_path

    def _build_content(
        self,
        use_case: UseCase,
    ) -> list:

        context = (
            build_documentation_context()
        )

        actor_name = (
            self._get_actor_name(
                use_case.primary_actor,
                context,
            )
        )

        requirement_labels = [
            self._get_requirement_label(
                requirement_id,
                context,
            )
            for requirement_id
            in use_case.related_requirements
        ]

        business_rule_labels = [
            self._get_business_rule_label(
                rule_id,
                context,
            )
            for rule_id
            in use_case.business_rules
        ]

        story = []

        story.append(
            Paragraph(
                (
                    f"{use_case.id} - "
                    f"{use_case.name}"
                ),
                self.styles[
                    "UseCaseTitle"
                ],
            )
        )

        story.append(
            Paragraph(
                "Información general",
                self.styles[
                    "SectionTitle"
                ],
            )
        )

        story.append(
            Paragraph(
                (
                    "<b>Identificador:</b> "
                    f"{use_case.id}"
                ),
                self.styles[
                    "Metadata"
                ],
            )
        )

        story.append(
            Paragraph(
                (
                    "<b>Actor principal:</b> "
                    f"{use_case.primary_actor} "
                    f"- {actor_name}"
                ),
                self.styles[
                    "Metadata"
                ],
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

    def _add_text_section(
        self,
        story: list,
        title: str,
        text: str,
    ) -> None:

        story.append(
            Paragraph(
                title,
                self.styles[
                    "SectionTitle"
                ],
            )
        )

        story.append(
            Paragraph(
                text.strip(),
                self.styles[
                    "BodyCustom"
                ],
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
                self.styles[
                    "SectionTitle"
                ],
            )
        )

        if not items:

            story.append(
                Paragraph(
                    "No definido.",
                    self.styles[
                        "BodyCustom"
                    ],
                )
            )

            return

        list_items = [
            ListItem(
                Paragraph(
                    item,
                    self.styles[
                        "BodyCustom"
                    ],
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
                self.styles[
                    "SectionTitle"
                ],
            )
        )

        if not items:

            story.append(
                Paragraph(
                    "No definido.",
                    self.styles[
                        "BodyCustom"
                    ],
                )
            )

            return

        list_items = [
            ListItem(
                Paragraph(
                    item,
                    self.styles[
                        "BodyCustom"
                    ],
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

        for requirement in context[
            "functional_requirements"
        ]:

            if (
                requirement["id"]
                == requirement_id
            ):

                return (
                    f'{requirement["id"]} - '
                    f'{requirement["name"]}'
                )

        return requirement_id

    def _get_business_rule_label(
        self,
        rule_id: str,
        context: dict,
    ) -> str:

        for rule in context[
            "business_rules"
        ]:

            if rule["id"] == rule_id:

                return (
                    f'{rule["id"]} - '
                    f'{rule["name"]}'
                )

        return rule_id
