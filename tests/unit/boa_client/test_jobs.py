from boa_client.jobs import BoaJob
from schema import SchemaError
import pytest
import os

def test_build_job_file_variable():
    '''
    Assert BuildJob file variable has expected file variable schema with a valid file
    '''
    expected = f'ci_valid.yaml'
    root = f'{os.getcwd()}/tests/unit/boa_client/test_cases'

    build_job = BoaJob(file=expected,
                       root=root)
    
    assert build_job.file == expected

def test_boa_job_invalid_file():
    '''
    Assert BuildJob raises a SchemaError on creation with a yaml file containing invalid schema
    '''
    expected = f'ci_invalid.yaml'
    root = f'{os.getcwd()}/tests/unit/boa_client/test_cases'

    with pytest.raises(SchemaError):
        boa_job = BoaJob(file=expected,
                         root=root)
        boa_job.execute_job()

def test_boa_execute_invalid_job_raises_system_exit():
    '''
    Assert BuildJob raises a SystemError on a non-zero return value from subprocess
    '''
    expected = f'ci_system_error.yaml'
    root = f'{os.getcwd()}/tests/unit/boa_client/test_cases'

    with pytest.raises(SystemError):
        boa_job = BoaJob(file=expected,
                         root=root)
        boa_job.execute_job()

def test_boa_execute_valid_job__does_not_raise_system_exit():
    '''
    Assert BuildJob does not raise a SystemError on a zero return value from subprocess
    '''
    expected = f'ci_no_system_error.yaml'
    root = f'{os.getcwd()}/tests/unit/boa_client/test_cases'

    try:
        boa_job = BoaJob(file=expected,
                         root=root)
        boa_job.execute_job()
    except SystemError as se:
        assert False, f"input test case raised an exception {se}"