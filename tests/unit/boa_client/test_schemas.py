from boa_client.schemas import BoaJobSchema
from schema import SchemaError
import pytest
import pathlib

cwd = pathlib.Path(__file__).parent.resolve()

def test_valid_build_job_schema():
    '''
    Assert BuildJobSchema input matches output when a valid test case is used
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

    try:
        build_job_schema = BoaJobSchema()
        build_job_schema.validate(expected)
    except SchemaError as se:
        assert False, f"input test case raised an exception {se}"

def test_invalid_build_job_schema():
    '''
    Assert BuildJobSchema raises a SchemaError on validation of input containing invalid schema
    '''

    input = {
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
        build_job_schema = BoaJobSchema()
        build_job_schema.validate(input)

