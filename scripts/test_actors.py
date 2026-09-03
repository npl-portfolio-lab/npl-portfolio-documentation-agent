from pathlib import Path

from agents.documentation_agent.loader import (
    load_actors,
)


path = Path(
    "requirements/actors.yaml"
)

actors = load_actors(path)

for actor in actors:
    print(
        actor.id,
        "-",
        actor.name,
    )
