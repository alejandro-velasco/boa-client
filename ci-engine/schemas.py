from schema import Schema, Regex, SchemaError

class BuildJobSchema:
    
    def __init__(self) -> None:
        self.schema = Schema({
            "apiVersion": str,
            "kind": "BuildJob",
            "metadata": {
                "name": str,
                "namespace": str,
            },
            "stages": {
                Regex(r"^[a-zA-Z0-9_]*$"): {
                    "script": str    
                }
            }
        })

    def validate(self, file):
        try:
            self.schema.validate(file)
        except SchemaError as se:
            raise se