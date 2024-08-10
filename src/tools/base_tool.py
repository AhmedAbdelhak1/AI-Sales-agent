from abc import ABC, abstractmethod
from instructor import OpenAISchema
from typing import Any

class BaseTool(ABC, OpenAISchema):
    @abstractmethod
    def run(self):
        pass
    
    # Remove "title" field for all tools parameters
    class Config:
        @staticmethod
        def json_schema_extra(schema: dict[str, Any], model: type['BaseTool']) -> None:
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)