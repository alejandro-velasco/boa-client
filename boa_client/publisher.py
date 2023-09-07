import os
import requests
import logging

class BoaClientPublisher:
    def __init__(self, name: str, server: str, execution_id: str, organization_id: str):
        self.server=server
        self.name = name
        self.execution_id = execution_id
        self.organization_id = organization_id

    def publish_success(self):
        url = f'{self.server}/api/job/status/{self.execution_id}'
        headers = {'Content-Type': 'application/json'}
        json = {'status': 'succeeded'}
        
        response = requests.put(url, 
                                json=json,
                                headers=headers)
        
        logging.info(response.text)

    def publish_failure(self):
        url = f'{self.server}/api/job/status/{self.execution_id}'
        headers = {'Content-Type': 'application/json'}
        json = {'status': 'failed'}
        
        response = requests.put(url, 
                                json=json,
                                headers=headers)
        
        logging.info(response.text)

    def publish_abort(self):
        url = f'{self.server}/api/job/status/{self.execution_id}'
        headers = {'Content-Type': 'application/json'}
        json = {'status': 'aborted'}
        
        response = requests.put(url, 
                            json=json,
                            headers=headers)
        
        logging.info(response.text)

    def publish_running(self):
        url = f'{self.server}/api/job/status/{self.execution_id}'
        headers = {'Content-Type': 'application/json'}
        json = {'status': 'running'}
        
        response = requests.put(url, 
                                json=json,
                                headers=headers)
        
        logging.info(response.text)