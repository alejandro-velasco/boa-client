import logging
import sys
from rich.console import Console
from rich.logging import RichHandler

class Logger:
    def __init__(self, level) -> None:
        self.level = level
        self._set_log_level(self.level)


    def _set_log_level(self, level):
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