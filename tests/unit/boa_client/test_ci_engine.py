from boa_client.jobs import BoaJob
from schema import SchemaError
import pytest
import pathlib

cwd = pathlib.Path(__file__).parent.resolve()

def test_build_job_file_variable():
    '''
    Assert BuildJob file variable has expected file variable schema with a valid file
    '''

    build_job = BoaJob(f'{cwd}/test_cases/ci_valid.yaml')

    expected = {
        'apiVersion': 'v1', 
        'kind': 'BoaJob', 
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
                    'echo deploying...'
                ]
            }
        }
    }

    assert build_job.file == expected

def test_boa_job_invalid_file():
    '''
    Assert BuildJob raises a SchemaError on creation with a yaml file containing invalid schema
    '''
    with pytest.raises(SchemaError):
        boa_job = BoaJob(f'{cwd}/test_cases/ci_invalid.yaml')
        boa_job.execute_job()

