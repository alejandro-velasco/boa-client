import logging
import rich
from schema import Schema, Regex, SchemaError

class BoaJobSchema:
    
    def __init__(self) -> None:
        self.step_keywords = ["script"]
        self.schema = Schema({
            "apiVersion": str,
            "kind": "BoaJob",
            "metadata": {
                "name": str,
                "namespace": str,
            },
            "stages": {
                # Any alphanumeric, or underscore character combination is valid
                Regex(r"^[a-zA-Z0-9_]*$"): {
                    # Any string defined in list 'self.step_keyword' is valid
                    Regex(fr"(?i)(\W|^)({'|'.join(self.step_keywords)})(\W|$)"): list
                }
            }
        })

    def validate(self, file):
        try:
            logging.info('Validating ci file...')
            data = self.schema.validate(file)
            logging.info('ci file valid!')
            return data
        except SchemaError as se:
            logging.error('ci file is Invalid!')
            raise se