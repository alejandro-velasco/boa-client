import yaml
import subprocess
import logging
import rich
from boa_client.schemas import BoaJobSchema

class BoaJob:
    def __init__(self, file) -> None:
        self.file = file
        
    def _validate_schema(self):
        build_job_schema = BoaJobSchema()
        build_job_schema.validate(self.file)

    def execute_job(self):
        self._validate_schema()
        stages = self.file['stages']

        for stage_name, stage_spec in stages.items():
            self.execute_stage(stage_name=stage_name, stage_spec=stage_spec)
    
    def execute_stage(self, stage_name, stage_spec):
        logging.info(f'Executing stage "{stage_name}"')

        for step_name, step_spec in stage_spec.items():
            if step_name == 'script':
                self.execute_script(step_spec)

    def execute_script(self, script):
        for step in script:
            logging.debug(f'\n{step}')
            p = subprocess.Popen([step], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
            output, errors = p.communicate()

            if p.returncode != 0:
                # handle error
                logging.error(errors)
                raise SystemExit(1)

            logging.info(f'{output}')
    

            
