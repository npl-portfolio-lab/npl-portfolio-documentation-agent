from .reference_resolver import ReferenceResolver


class DataModelRenderer:
    """
    Genera documentación Markdown del modelo lógico de datos
    a partir del contexto estructurado del proyecto.
    """

    def __init__(self, context: dict):
        self.context = context
        self.resolver = ReferenceResolver(context)

        data_model = context.get("data_model", {})
        self.entities = data_model.get("entities", [])

        self.entity_index = {
            entity["id"]: entity
            for entity in self.entities
        }

    def render(self) -> str:
        lines = []

        project = self.context.get("project", {})

        lines.append("# Modelo Lógico de Datos")
        lines.append("")

        if project:
            lines.append(
                f"**Proyecto:** {project.get('name', 'N/A')}"
            )
            lines.append("")

            objective = project.get("objective")

            if objective:
                lines.append("## Objetivo del proyecto")
                lines.append("")
                lines.append(objective)
                lines.append("")

        lines.append("## Entidades")
        lines.append("")

        for entity in self.entities:
            lines.extend(
                self._render_entity(entity)
            )

        lines.extend(
            self._render_relationship_diagram()
        )

        lines.extend(
            self._render_traceability_matrix()
        )

        return "\n".join(lines)

    def _render_entity(self, entity: dict) -> list[str]:
        lines = []

        lines.append(
            f"### {entity['id']} - {entity['name']}"
        )
        lines.append("")
        lines.append(entity["description"].strip())
        lines.append("")

        lines.extend(
            self._render_fields(
                entity.get("fields", [])
            )
        )

        lines.extend(
            self._render_constraints(
                entity.get("constraints", [])
            )
        )

        lines.extend(
            self._render_relationships(
                entity.get("relationships", [])
            )
        )

        lines.extend(
            self._render_references(
                entity
            )
        )

        lines.append("---")
        lines.append("")

        return lines

    def _render_fields(
        self,
        fields: list[dict],
    ) -> list[str]:
        lines = []

        lines.append("#### Campos")
        lines.append("")

        if not fields:
            lines.append(
                "No se han definido campos."
            )
            lines.append("")
            return lines

        lines.append(
            "| Campo | Tipo | Nullable | Descripción |"
        )
        lines.append(
            "|---|---|---|---|"
        )

        for field in fields:
            nullable = (
                "Sí"
                if field.get("nullable", True)
                else "No"
            )

            lines.append(
                f"| {field['name']} "
                f"| {field['type']} "
                f"| {nullable} "
                f"| {field['description']} |"
            )

        lines.append("")

        return lines

    def _render_constraints(
        self,
        constraints: list[str],
    ) -> list[str]:
        lines = []

        lines.append("#### Restricciones")
        lines.append("")

        if not constraints:
            lines.append(
                "No se han definido restricciones."
            )
            lines.append("")
            return lines

        for constraint in constraints:
            lines.append(
                f"- {constraint}"
            )

        lines.append("")

        return lines

    def _render_relationships(
        self,
        relationships: list[dict],
    ) -> list[str]:
        lines = []

        lines.append("#### Relaciones")
        lines.append("")

        if not relationships:
            lines.append(
                "No se han definido relaciones."
            )
            lines.append("")
            return lines

        for relationship in relationships:
            target_id = relationship[
                "target_entity"
            ]

            target = self.entity_index.get(
                target_id
            )

            if target:
                target_name = (
                    f"{target_id} - "
                    f"{target['name']}"
                )
            else:
                target_name = target_id

            relationship_type = (
                relationship["type"]
                .replace("_", " ")
            )

            lines.append(
                f"- **{relationship_type}** "
                f"→ {target_name}: "
                f"{relationship['description']}"
            )

        lines.append("")

        return lines

    def _render_references(
        self,
        entity: dict,
    ) -> list[str]:
        lines = []

        lines.append("#### Trazabilidad")
        lines.append("")

        requirements = entity.get(
            "related_requirements",
            [],
        )

        use_cases = entity.get(
            "related_use_cases",
            [],
        )

        business_rules = entity.get(
            "related_business_rules",
            [],
        )

        lines.append(
            "**Requerimientos funcionales:**"
        )
        lines.append("")

        if requirements:
            for requirement_id in requirements:
                requirement = (
                    self.resolver.get_requirement(
                        requirement_id
                    )
                )

                lines.append(
                    f"- {requirement['id']} - "
                    f"{requirement['name']}"
                )
        else:
            lines.append("- Ninguno.")

        lines.append("")
        lines.append(
            "**Casos de uso:**"
        )
        lines.append("")

        if use_cases:
            for use_case_id in use_cases:
                use_case = (
                    self.resolver.get_use_case(
                        use_case_id
                    )
                )

                lines.append(
                    f"- {use_case['id']} - "
                    f"{use_case['name']}"
                )
        else:
            lines.append("- Ninguno.")

        lines.append("")
        lines.append(
            "**Reglas de negocio:**"
        )
        lines.append("")

        if business_rules:
            for rule_id in business_rules:
                rule = (
                    self.resolver.get_business_rule(
                        rule_id
                    )
                )

                lines.append(
                    f"- {rule['id']} - "
                    f"{rule['name']}"
                )
        else:
            lines.append("- Ninguna.")

        lines.append("")

        return lines

    def _render_relationship_diagram(
        self,
    ) -> list[str]:
        lines = []

        lines.append(
            "## Diagrama lógico de relaciones"
        )
        lines.append("")
        lines.append("```mermaid")
        lines.append("erDiagram")

        rendered = set()

        for entity in self.entities:
            source_name = entity[
                "name"
            ].replace(" ", "_")

            for relationship in entity.get(
                "relationships",
                [],
            ):
                target = self.entity_index.get(
                    relationship["target_entity"]
                )

                if not target:
                    continue

                target_name = target[
                    "name"
                ].replace(" ", "_")

                pair = tuple(
                    sorted(
                        [
                            source_name,
                            target_name,
                        ]
                    )
                )

                if pair in rendered:
                    continue

                rendered.add(pair)

                relation_type = relationship[
                    "type"
                ]

                if relation_type == "one_to_many":
                    symbol = "||--o{"
                elif relation_type == "many_to_one":
                    symbol = "}o--||"
                elif relation_type == "many_to_one_optional":
                    symbol = "}o--o|"
                elif relation_type == "one_to_one":
                    symbol = "||--||"
                else:
                    symbol = "}o--o{"

                lines.append(
                    f'    {source_name} '
                    f'{symbol} '
                    f'{target_name} : '
                    f'"relaciona"'
                )

        lines.append("```")
        lines.append("")

        return lines

    def _render_traceability_matrix(
        self,
    ) -> list[str]:
        lines = []

        lines.append(
            "## Matriz de trazabilidad"
        )
        lines.append("")

        lines.append(
            "| Entidad | Requerimientos | "
            "Casos de uso | Reglas de negocio |"
        )

        lines.append(
            "|---|---|---|---|"
        )

        for entity in self.entities:
            requirements = ", ".join(
                entity.get(
                    "related_requirements",
                    [],
                )
            ) or "-"

            use_cases = ", ".join(
                entity.get(
                    "related_use_cases",
                    [],
                )
            ) or "-"

            rules = ", ".join(
                entity.get(
                    "related_business_rules",
                    [],
                )
            ) or "-"

            lines.append(
                f"| {entity['id']} - "
                f"{entity['name']} "
                f"| {requirements} "
                f"| {use_cases} "
                f"| {rules} |"
            )

        lines.append("")

        return lines
