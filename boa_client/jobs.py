import yaml
import subprocess
import logging
import rich
from boa_client.schemas import BoaJobSchema

class BoaJob:
    def __init__(self, file) -> None:
        self.file = self._get_file(file)

    def _get_file(self, file):
        with open(file) as f:
            # use safe_load instead load
            return yaml.safe_load(f)
        
    def _validate_schema(self):
        build_job_schema = BoaJobSchema()
        build_job_schema.validate(self.file)

    def execute_job(self):
        self._validate_schema()
        stages = self.file['stages']

        for stage_name, stage_spec in stages.items():
            self.execute_stage(stage_name, stage_spec)
    
    def execute_stage(self, stage_name, stage_spec):
        logging.info(f'Executing stage "{stage_name}"')

        for step in stage_spec['script']:
            logging.debug(f'\n{step}')
            p = subprocess.Popen([step], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
            output, errors = p.communicate()

            if p.returncode != 0:
                # handle error
                logging.error(errors)
                raise SystemExit(1)

            logging.info(f'{output}')
    

            