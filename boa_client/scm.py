import subprocess
import logging
import rich

class GitClient:
    def __init__(self, repos) -> None:
        self.repos = repos
    
    def checkout_scm(self):
        for repo in self.repos:
            cmd = ["git", "clone", repo["url"]]
            
            if "submodules" in repo:
               cmd.append("--recurse-submodules")
            if "branch"in repo:
                cmd = cmd + ["--branch", repo["branch"]]
            if "name" in repo:
                cmd.append(repo["name"])

            logging.info(f"Cloning {repo['url']}")
            logging.debug(" ".join(cmd))
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
            output, errors = p.communicate()

            if p.returncode != 0:
                # handle error
                logging.error(errors)
                raise SystemExit(1)

            logging.info(f'{output}')


    

            
