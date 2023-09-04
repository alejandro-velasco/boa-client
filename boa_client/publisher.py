import os
import redis
import logging

class BoaClientPublisher:
    def __init__(self, name: str):
        # connect with redis server
        self.client = redis.Redis(host=os.getenv('REDIS_HOSTNAME'), 
                                  port=os.getenv('REDIS_PORT', '6379'), 
                                  db=0)
        self.name = name

    def publish_success(self):
        self.client.publish(self.name, 'SUCCEEDED')

    def publish_failure(self):
        self.client.publish(self.name, 'FAILED')

    def publish_abort(self):
        self.client.publish(self.name, 'ABORTED')

    def publish_running(self):
        self.client.publish(self.name, 'RUNNING')