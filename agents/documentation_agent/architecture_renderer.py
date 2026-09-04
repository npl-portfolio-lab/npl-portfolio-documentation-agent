from .reference_resolver import ReferenceResolver


class ArchitectureRenderer:
    """
    Genera documentación Markdown de arquitectura
    utilizando las fuentes estructuradas del proyecto.
    """

    def __init__(self, context: dict):
        self.context = context
        self.resolver = ReferenceResolver(context)

    def render(self) -> str:
        """
        Genera el documento completo de arquitectura.
        """
        project = self.context["project"]
        architecture = self.context["architecture"]

        lines = []

        lines.append(
            f"# Arquitectura del sistema - {project['name']}"
        )
        lines.append("")

        lines.append("## Objetivo")
        lines.append("")
        lines.append(
            "Definir la arquitectura lógica inicial del sistema "
            "NPL, relacionando cada componente con los "
            "requerimientos funcionales, casos de uso y reglas "
            "de negocio que justifican su existencia."
        )
        lines.append("")

        lines.append("## Componentes arquitectónicos")
        lines.append("")

        for component in architecture["components"]:
            self._render_component(
                component,
                lines,
            )

        lines.append("## Componentes transversales")
        lines.append("")

        for component in architecture[
            "cross_cutting_components"
        ]:
            self._render_component(
                component,
                lines,
            )

        self._render_traceability_matrix(lines)

        return "\n".join(lines)

    def _render_component(
        self,
        component: dict,
        lines: list[str],
    ) -> None:
        """
        Renderiza un componente arquitectónico
        y todas sus referencias relacionadas.
        """
        lines.append(
            f"### {component['id']} - {component['name']}"
        )
        lines.append("")
        lines.append(component["description"].strip())
        lines.append("")

        self._render_requirements(
            component["related_requirements"],
            lines,
        )

        self._render_use_cases(
            component["related_use_cases"],
            lines,
        )

        self._render_business_rules(
            component["related_business_rules"],
            lines,
        )

        lines.append("---")
        lines.append("")

    def _render_requirements(
        self,
        requirement_ids: list[str],
        lines: list[str],
    ) -> None:
        if not requirement_ids:
            return

        lines.append("#### Requerimientos funcionales relacionados")
        lines.append("")

        for requirement_id in requirement_ids:
            requirement = self.resolver.get_requirement(
                requirement_id
            )

            lines.append(
                f"##### {requirement['id']} - "
                f"{requirement['name']}"
            )
            lines.append("")
            lines.append(
                requirement["description"].strip()
            )
            lines.append("")
            lines.append(
                f"**Prioridad:** {requirement['priority']}"
            )
            lines.append("")
            lines.append(
                f"**Estado:** {requirement['status']}"
            )
            lines.append("")

    def _render_use_cases(
        self,
        use_case_ids: list[str],
        lines: list[str],
    ) -> None:
        if not use_case_ids:
            return

        lines.append("#### Casos de uso relacionados")
        lines.append("")

        for use_case_id in use_case_ids:
            use_case = self.resolver.get_use_case(
                use_case_id
            )

            lines.append(
                f"##### {use_case['id']} - "
                f"{use_case['name']}"
            )
            lines.append("")
            lines.append(
                use_case["objective"].strip()
            )
            lines.append("")

    def _render_business_rules(
        self,
        rule_ids: list[str],
        lines: list[str],
    ) -> None:
        if not rule_ids:
            return

        lines.append("#### Reglas de negocio relacionadas")
        lines.append("")

        for rule_id in rule_ids:
            rule = self.resolver.get_business_rule(
                rule_id
            )

            lines.append(
                f"##### {rule['id']} - "
                f"{rule['name']}"
            )
            lines.append("")
            lines.append(
                rule["description"].strip()
            )
            lines.append("")
            lines.append(
                f"**Categoría:** {rule['category']}"
            )
            lines.append("")
            lines.append(
                f"**Prioridad:** {rule['priority']}"
            )
            lines.append("")

    def _render_traceability_matrix(
        self,
        lines: list[str],
    ) -> None:
        """
        Genera la matriz de trazabilidad entre
        arquitectura, RF y CU.
        """
        lines.append("## Matriz de trazabilidad")
        lines.append("")

        lines.append(
            "| Componente | Requerimiento funcional | Caso de uso |"
        )
        lines.append(
            "|---|---|---|"
        )

        architecture = self.context["architecture"]

        for component in architecture["components"]:
            requirement_ids = component[
                "related_requirements"
            ]

            use_case_ids = component[
                "related_use_cases"
            ]

            requirement_text = ", ".join(
                self._requirement_label(
                    requirement_id
                )
                for requirement_id in requirement_ids
            )

            use_case_text = ", ".join(
                self._use_case_label(
                    use_case_id
                )
                for use_case_id in use_case_ids
            )

            component_text = (
                f"{component['id']} - "
                f"{component['name']}"
            )

            lines.append(
                f"| {component_text} | "
                f"{requirement_text} | "
                f"{use_case_text} |"
            )

        lines.append("")

    def _requirement_label(
        self,
        requirement_id: str,
    ) -> str:
        requirement = self.resolver.get_requirement(
            requirement_id
        )

        return (
            f"{requirement['id']} - "
            f"{requirement['name']}"
        )

    def _use_case_label(
        self,
        use_case_id: str,
    ) -> str:
        use_case = self.resolver.get_use_case(
            use_case_id
        )

        return (
            f"{use_case['id']} - "
            f"{use_case['name']}"
        )
