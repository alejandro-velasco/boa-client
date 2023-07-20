from ci_engine.jobs import BuildJob
import pathlib

cwd = pathlib.Path(__file__).parent.resolve()

def test_expected_output():

    build_job = BuildJob(f'{cwd}/test_cases/ci_valid.yaml')

    expected = {
        'apiVersion': 'v1', 
        'kind': 'BuildJob', 
        'metadata': {
            'name': 'test-build', 
            'namespace': 'test'
        }, 'stages': {
            'build': {
                'script': [
                    'echo building...\n'
                ]
            }, 
            'deploy': {
                'script': [
                    'echo deploying...\n'
                ]
            }
        }
    }

    assert build_job.file == expected