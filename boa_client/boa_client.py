import logging
import typer
from typing_extensions import Annotated
from rich.console import Console
from rich.logging import RichHandler
import sys
import os
import yaml
from boa_client.jobs import BoaJob
from boa_client.scm import clone

def set_log_level(level):
    if level == 'INFO':
        log_level=logging.INFO
    elif level == 'WARN':
        log_level=logging.WARN
    elif level == 'DEBUG':
        log_level=logging.DEBUG
    else:
        logging.error('Log level {level} is not a valid option. Please choose between "INFO", "WARN" or "DEBUG"')
        sys.exit(1)

    stderr = Console(file=sys.stderr)
    logging.basicConfig(level=log_level,
                        format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
                        handlers=[RichHandler(console=stderr)])

def main(    
    repository: Annotated[str, typer.Option()],
    submodules: bool = False,
    branch: str = "",
    name: str = "workspace",
    file: str = 'boa.yaml',
    log_level: str = 'INFO'
):
    set_log_level(log_level)    

    # Checkout repository
    clone(url=repository,
          submodules=submodules,
          branch=branch,
          name=name)
    
    # Changing Current Working Directory to git repository
    cwd = os.getcwd()
    logging.info(f'Setting current working directory to {cwd}/{name}')
    os.chdir(f'{cwd}/{name}')

    # Read and execute boa job
    with open(file) as f:
        # use safe_load instead load
        build_job = BoaJob(file=yaml.safe_load(f))
        build_job.execute_job()

def entrypoint():
    typer.run(main)

if __name__ == "__main__":
    typer.run(main)