import typer
import os
import logging
from typing_extensions import Annotated
from boa_client.jobs import BoaJob
from boa_client.scm import GitRepository
from boa_client.logging import Logger
from boa_client.publisher import BoaClientPublisher
def main(    
    url: Annotated[str, typer.Option()],
    name: Annotated[str, typer.Option()],
    execution_id: Annotated[str, typer.Option()],
    organization_id: Annotated[str, typer.Option()],
    server: Annotated[str, typer.Option()],
    submodules: bool = False,
    branch: str = "",
    file: str = 'boa.yaml',
    log_level: str = 'INFO'
):
    logger = Logger(level=log_level)

    publisher = BoaClientPublisher(server=server,
                                   name=name,
                                   execution_id=execution_id,
                                   organization_id=organization_id)
    publisher.publish_running()

    try:
        repository = GitRepository(url=url)
        repository.clone(submodules=submodules,
                         branch=branch,
                         name=name)
        
        root = f'{os.getcwd()}/{name}'
        build_job = BoaJob(file=file, 
                           root=root)
        build_job.execute_job()
        publisher.publish_success()
    except Exception as e:
        publisher.publish_failure()
        logging.error(f'An Exception has occurred: {e}')
        raise e

def entrypoint():
    typer.run(main)

if __name__ == "__main__":
    typer.run(main)