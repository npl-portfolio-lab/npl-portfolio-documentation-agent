from pydantic import BaseModel
from typing import Literal


class FunctionalRequirement(BaseModel):
    id: str
    name: str
    description: str
    priority: Literal["low", "medium", "high"]
    status: Literal["draft", "review", "approved", "deprecated"]


class Actor(BaseModel):
    id: str
    name: str
    description: str


class BusinessRule(BaseModel):
    id: str
    name: str
    description: str
    category: str
    priority: Literal[
        "low",
        "medium",
        "high",
    ]


class UseCaseDefinition(BaseModel):
    id: str
    related_requirement: str
    primary_actor: str
    name: str
    objective: str
    preconditions: list[str]
    main_flow: list[str]
    alternative_flows: list[str]
    postconditions: list[str]
    business_rules: list[str]


class UseCase(BaseModel):
    id: str
    name: str
    primary_actor: str
    objective: str
    preconditions: list[str]
    main_flow: list[str]
    alternative_flows: list[str]
    postconditions: list[str]
    related_requirements: list[str]
    business_rules: list[str]
