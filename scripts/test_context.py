from pprint import pprint

from agents.documentation_agent.context_builder import (
    build_documentation_context,
)


context = build_documentation_context()

pprint(context)
