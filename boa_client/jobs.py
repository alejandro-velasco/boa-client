import yaml
import subprocess
import logging
import os
from boa_client.scm import GitRepository
from boa_client.schemas import BoaJobSchema


class BoaJob:
    def __init__(self, file, root) -> None:
        self.root = root
        self.cwd = os.getcwd()
        self.file = file
        self.body = self._load_file()

    def _load_file(self):
        with open(f'{self.root}/{self.file}') as f:
            return yaml.safe_load(f)

    def _validate_schema(self):
        build_job_schema = BoaJobSchema()
        build_job_schema.validate(self.body)

    def _set_root(self):
        logging.info(f'Setting current working directory to {self.root}')
        os.chdir(self.root)        

    def _return_to_cwd(self):
        logging.info(f'Setting current working directory to {self.cwd}')
        os.chdir(self.cwd)  

    def execute_job(self):
        try:
            self._validate_schema()
            self._set_root()
            self._load_file()

            if "git" in self.body:
                for git_config in self.body['git']:
                    repository = GitRepository(url=git_config.get("url"))
                    repository.clone(submodules=git_config.get("submodules", False),
                                     branch=git_config.get("branch", ""),
                                     name=git_config.get("name", ""))
            
            stages = self.body['stages']
            
            for stage_name, stage_spec in stages.items():
                self.execute_stage(stage_name=stage_name, stage_spec=stage_spec)
        finally:
            self._return_to_cwd()

    def execute_stage(self, stage_name, stage_spec):
        logging.info(f'Executing stage "{stage_name}"')

        for step_name, step_spec in stage_spec.items():
            if step_name == 'script':
                self.execute_script(step_spec)

    def execute_script(self, script):
        for step in script:
            logging.debug(f'\n{step}')
            p = subprocess.Popen([step], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE, 
                                 shell=True, 
                                 text=True)
    
            output, errors = p.communicate()

            if p.returncode != 0:
                # handle error
                logging.error(errors)
                raise SystemError

            logging.info(f'{output}')
    

            
