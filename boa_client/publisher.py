import os
import requests
import logging

class BoaClientPublisher:
    def __init__(self, name: str, server: str, execution: str, organization_id: str):
        self.server=server
        self.name = name
        self.execution = execution
        self.organization_id = organization_id

    def publish_success(self):
        url = f'{self.server}/api/jobs/status'
        headers = {'Content-Type': 'application/json'}
        json = {
            'organization_id': self.organization_id,
            'execution': self.execution,
            'job_name': self.name,
            'status': 'succeeded'
        }
        
        resp = requests.put(url, 
                            json=json,
                            headers=headers)
        
        logging.info(resp.text)

    def publish_failure(self):
        url = f'{self.server}/api/jobs/status'
        headers = {'Content-Type': 'application/json'}
        json = {
            'organization_id': self.organization_id,
            'execution': self.execution,
            'job_name': self.name,
            'status': 'failed'
        }
        
        resp = requests.put(url, 
                            json=json,
                            headers=headers)
        
        logging.info(resp.text)

    def publish_abort(self):
        url = f'{self.server}/api/jobs/status'
        headers = {'Content-Type': 'application/json'}
        json = {
            'organization_id': self.organization_id,
            'execution': self.execution,
            'job_name': self.name,
            'status': 'aborted'
        }
        
        resp = requests.put(url, 
                            json=json,
                            headers=headers)
        
        logging.info(resp.text)

    def publish_running(self):
        url = f'{self.server}/api/jobs/status'
        headers = {'Content-Type': 'application/json'}
        json = {
            'organization_id': self.organization_id,
            'execution': self.execution,
            'job_name': self.name,
            'status': 'running'
        }
        
        resp = requests.put(url, 
                            json=json,
                            headers=headers)
        
        logging.info(resp.text)