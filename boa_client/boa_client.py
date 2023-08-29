import typer
import os
from typing_extensions import Annotated
from boa_client.jobs import BoaJob
from boa_client.scm import GitRepository
from boa_client.logging import Logger

def main(    
    url: Annotated[str, typer.Option()],
    submodules: bool = False,
    branch: str = "",
    name: str = "workspace",
    file: str = 'boa.yaml',
    log_level: str = 'INFO'
):
    logger = Logger(level=log_level)   
    repository = GitRepository(url=url)
    repository.clone(submodules=submodules,
                     branch=branch,
                     name=name)

    # Read and execute boa job
    build_job = BoaJob(file=file, 
                       root=f'{os.getcwd()}/{name}')
    build_job.execute_job()

def entrypoint():
    typer.run(main)

if __name__ == "__main__":
    typer.run(main)