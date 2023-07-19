import yaml
from schemas import BuildJobSchema

class DSLParser:
    def __init__(self, file) -> None:
        self.file = self._get_file(file)
        self._validate_schema()

    def _get_file(self, file):
        with open(file) as f:
            # use safe_load instead load
            return yaml.safe_load(f)
        
    def _validate_schema(self):
        build_job_schema = BuildJobSchema()
        build_job_schema.validate(self.file)
