from parser import DSLParser
from executor import BuildJobExecutor

def main():
    dsl = DSLParser(file='/mnt/c/Users/aleja/OneDrive/Documents/ci-orchestrator/ci-engine/test/ci.yaml')
    
    print(dsl.file)

if __name__ == "__main__":
    main()