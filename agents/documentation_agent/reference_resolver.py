class ReferenceResolver:
    """
    Resuelve referencias entre los diferentes elementos
    estructurados de la documentación del proyecto.
    """

    def __init__(self, context: dict):
        self.context = context

        # Índices para búsquedas rápidas por ID.
        self.requirements = self._build_index(
            context["functional_requirements"]
        )

        self.business_rules = self._build_index(
            context["business_rules"]
        )

        self.use_cases = self._build_index(
            context["use_case_definitions"]
        )

        self.actors = self._build_index(
            context["actors"]
        )

    @staticmethod
    def _build_index(items: list[dict]) -> dict:
        """
        Convierte una lista de elementos en un diccionario
        indexado por su identificador.
        """
        return {
            item["id"]: item
            for item in items
        }

    def get_requirement(self, requirement_id: str) -> dict:
        """
        Obtiene un requerimiento funcional por ID.
        """
        if requirement_id not in self.requirements:
            raise ValueError(
                f"Requerimiento no encontrado: {requirement_id}"
            )

        return self.requirements[requirement_id]

    def get_business_rule(self, rule_id: str) -> dict:
        """
        Obtiene una regla de negocio por ID.
        """
        if rule_id not in self.business_rules:
            raise ValueError(
                f"Regla de negocio no encontrada: {rule_id}"
            )

        return self.business_rules[rule_id]

    def get_use_case(self, use_case_id: str) -> dict:
        """
        Obtiene un caso de uso por ID.
        """
        if use_case_id not in self.use_cases:
            raise ValueError(
                f"Caso de uso no encontrado: {use_case_id}"
            )

        return self.use_cases[use_case_id]

    def get_actor(self, actor_id: str) -> dict:
        """
        Obtiene un actor por ID.
        """
        if actor_id not in self.actors:
            raise ValueError(
                f"Actor no encontrado: {actor_id}"
            )

        return self.actors[actor_id]
