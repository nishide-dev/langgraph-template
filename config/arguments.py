# external imports
from argparse import ArgumentParser

from pydantic import BaseModel, Field

# internal imports


class Arguments(BaseModel):
    """Arguments class for the main script."""

    # name
    name: str = Field(
        default="Langgraph Template",
        title="n",
        description="name",
    )

    @classmethod
    def parse_args(cls: "Arguments"):  # noqa: ANN206
        """Parse arguments."""
        parser = ArgumentParser()
        properties: dict = cls.model_json_schema()["properties"]
        for v in properties.values():
            arg = {}
            arg["name_or_flags"] = [f"-{v['title']}", f"--{v['description']}"]
            if v["type"] == "boolean":
                arg["action"] = "store_true" if not v["default"] else "store_false"
            else:
                if v["default"]:
                    arg["default"] = v["default"]
                else:
                    arg["required"] = True
                if v["description"]:
                    arg["help"] = v["description"]
                if v["type"]:
                    if v["type"] == "array":
                        arg["nargs"] = "*"
                        arg["type"] = cls._convert_json_schema_type_to_argparse_type(
                            v["items"]["type"]
                        )
                    else:
                        arg["type"] = cls._convert_json_schema_type_to_argparse_type(
                            v["type"]
                        )

            if v["type"] == "boolean":
                parser.add_argument(
                    *arg["name_or_flags"],
                    action=arg["action"],
                    help=v.get("description"),
                )
            else:
                parser.add_argument(
                    *arg["name_or_flags"],
                    default=arg.get("default"),
                    help=arg.get("help"),
                    type=arg.get("type"),
                    required=arg.get("required"),
                    nargs=arg.get("nargs"),
                )
        return cls.model_validate(parser.parse_args().__dict__)

    @staticmethod
    def _convert_json_schema_type_to_argparse_type(json_schema_type: str) -> type:
        """Convert JSON schema type to argparse type."""
        if json_schema_type == "string":
            return str
        if json_schema_type == "integer":
            return int
        if json_schema_type == "number":
            return float
        if json_schema_type == "boolean":
            return bool
        if json_schema_type == "array":
            return list
        value_error = f"Invalid JSON schema type: {json_schema_type}"
        raise ValueError(value_error)
