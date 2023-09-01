import subprocess
import logging
import rich

class GitRepository:

    def __init__(self, url) -> None:
        self.url = url

    def clone(self, submodules=False, branch="", name=""):
        cmd = ["git", "clone", self.url]
        if submodules:
           cmd.append("--recurse-submodules")
        if branch:
            cmd = cmd + ["--branch", branch]
        if name:
            cmd.append(name)
    
        logging.info(f"Cloning {self.url}")
        logging.debug(" ".join(cmd))
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        output, errors = p.communicate()
    
        if p.returncode != 0:
            # handle error
            logging.error(errors)
            raise SystemExit(1)
    
        logging.info(f'{output}')


    

            
