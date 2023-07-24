import logging
import typer
from rich.console import Console
from rich.logging import RichHandler
import sys
import yaml
from boa_client.jobs import BoaJob

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

def main(file: str, log_level: str = 'INFO'):
    set_log_level(log_level)
    with open(file) as f:
        # use safe_load instead load
        build_job = BoaJob(file=yaml.safe_load(f))
        build_job.execute_job()

def entrypoint():
    typer.run(main)

if __name__ == "__main__":
    typer.run(main)