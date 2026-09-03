from pprint import pprint

from agents.documentation_agent.agent import (
    DocumentationAgent,
)
from tests.fake_llm_client import (
    FakeLLMClient,
)


client = FakeLLMClient()

agent = DocumentationAgent(
    llm_client=client
)

use_case = agent.generate_use_case(
    "RF-001"
)

pprint(
    use_case.model_dump()
)
