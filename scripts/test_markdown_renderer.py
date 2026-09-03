from agents.documentation_agent.agent import (
    DocumentationAgent,
)
from agents.documentation_agent.markdown_renderer import (
    MarkdownRenderer,
)
from tests.fake_llm_client import (
    FakeLLMClient,
)


client = FakeLLMClient()

agent = DocumentationAgent(
    llm_client=client,
)

use_case = agent.generate_use_case(
    "RF-001"
)

renderer = MarkdownRenderer()

output_path = renderer.render_use_case(
    use_case
)

print(
    f"Markdown generado correctamente: {output_path}"
)
