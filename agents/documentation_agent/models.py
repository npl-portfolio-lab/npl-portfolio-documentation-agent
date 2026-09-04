from pydantic import BaseModel, Field
from typing import Literal


class FunctionalRequirement(BaseModel):
    id: str
    name: str
    description: str
    priority: Literal["low", "medium", "high"]
    status: Literal[
        "draft",
        "review",
        "approved",
        "deprecated",
    ]


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


class ArchitectureComponent(BaseModel):
    id: str
    name: str
    description: str

    related_requirements: list[str] = Field(default_factory=list)

    related_use_cases: list[str] = Field(default_factory=list)

    related_business_rules: list[str] = Field(default_factory=list)


class ArchitectureDefinition(BaseModel):
    components: list[ArchitectureComponent]

    cross_cutting_components: list[ArchitectureComponent] = Field(default_factory=list)


class DataField(BaseModel):
    name: str
    type: str
    nullable: bool
    description: str


class DataRelationship(BaseModel):
    target_entity: str

    type: Literal[
        "one_to_one",
        "one_to_many",
        "many_to_one",
        "many_to_many",
        "many_to_one_optional",
    ]

    description: str


class DataEntity(BaseModel):
    id: str
    name: str
    description: str

    fields: list[DataField] = Field(default_factory=list)

    constraints: list[str] = Field(default_factory=list)

    relationships: list[DataRelationship] = Field(default_factory=list)

    related_requirements: list[str] = Field(default_factory=list)

    related_use_cases: list[str] = Field(default_factory=list)

    related_business_rules: list[str] = Field(default_factory=list)


class DataModelDefinition(BaseModel):
    entities: list[DataEntity]
