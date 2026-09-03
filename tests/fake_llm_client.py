import json
import re

from agents.documentation_agent.llm_client import (
    LLMClient,
)


class FakeLLMClient(LLMClient):

    def generate(self, prompt: str) -> str:

        requirement_match = re.search(
            r'"id": "(RF-\d+)"',
            prompt,
        )

        if not requirement_match:
            raise ValueError("No se encontró un requirement_id en el prompt.")

        requirement_id = requirement_match.group(1)

        use_case_definition_match = re.search(
            r"USE CASE DEFINITION:\s*(\{.*\})\s*$",
            prompt,
            re.DOTALL,
        )

        if not use_case_definition_match:
            raise ValueError("No se encontró USE CASE DEFINITION en el prompt.")

        use_case_definition_json = use_case_definition_match.group(1)

        use_case_definition = json.loads(use_case_definition_json)

        response = {
            "id": use_case_definition["id"],
            "name": use_case_definition["name"],
            "primary_actor": (use_case_definition["primary_actor"]),
            "objective": (use_case_definition["objective"]),
            "preconditions": (use_case_definition["preconditions"]),
            "main_flow": (use_case_definition["main_flow"]),
            "alternative_flows": (use_case_definition["alternative_flows"]),
            "postconditions": (use_case_definition["postconditions"]),
            "related_requirements": [requirement_id],
            "business_rules": (use_case_definition["business_rules"]),
        }

        return json.dumps(
            response,
            ensure_ascii=False,
        )
