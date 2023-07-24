from boa_client.jobs import BoaJob
from schema import SchemaError
import pytest

def test_build_job_file_variable():
    '''
    Assert BuildJob file variable has expected file variable schema with a valid file
    '''
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

    build_job = BoaJob(file=expected)
    
    assert build_job.file == expected

def test_boa_job_invalid_file():
    '''
    Assert BuildJob raises a SchemaError on creation with a yaml file containing invalid schema
    '''
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
                'sccript': [
                    'echo deploying...'
                ]
            }
        }
    }

    with pytest.raises(SchemaError):
        boa_job = BoaJob(file=expected)
        boa_job.execute_job()

def test_boa_execute_invalid_job_raises_system_exit():
    '''
    Assert BuildJob raises a SystemExit on a non-zero return value from subprocess
    '''
    expected = {
        'apiVersion': 'v1', 
        'kind': 'BoaJob', 
        'metadata': {
            'name': 'test-build', 
            'namespace': 'test'
        }, 'stages': {
            'build': {
                'script': [
                    'false'
                ]
            }
        }
    }

    with pytest.raises(SystemExit):
        boa_job = BoaJob(file=expected)
        boa_job.execute_job()

def test_boa_execute_valid_job__does_not_raise_system_exit():
    '''
    Assert BuildJob does not raise a SystemExit on a zero return value from subprocess
    '''
    expected = {
        'apiVersion': 'v1', 
        'kind': 'BoaJob', 
        'metadata': {
            'name': 'test-build', 
            'namespace': 'test'
        }, 
        'stages': {
            'build': {
                'script': [
                    'true'
                ]
            }
        }
    }

    try:
        boa_job = BoaJob(file=expected)
        boa_job.execute_job()
    except SystemExit as se:
        assert False, f"input test case raised an exception {se}"