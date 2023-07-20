import logging
import rich
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
                    "script": list
                }
            }
        })

    def validate(self, file):
        try:
            logging.info('Validating ci file...')
            self.schema.validate(file)
            logging.info('ci file valid!')
        except SchemaError as se:
            logging.error('ci file is Invalid!')
            raise se