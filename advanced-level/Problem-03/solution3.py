import json
from jsonschema import validate, ValidationError


schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["id", "name", "email"],
    "additionalProperties": False
}


json_input = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}

def validate_json(input_data, schema):
    try:
        validate(instance=input_data, schema=schema)
        print("JSON is valid ✅")
        return True
    except ValidationError as e:
        print("JSON validation error ❌")
        print(e.message)
        return False


validate_json(json_input, schema)
