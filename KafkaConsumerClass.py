import os
import sys
sys.path.append(f"{os.getcwd()}/libs")


from confluent_kafka.admin import AdminClient, NewTopic  # noqa: E402
import certifi  # noqa: E402
from confluent_kafka import Consumer, KafkaError  # noqa: E402
import ccloud_lib
import json

class KafkaConsumer:
    def __init__(self, config_file_location):
        self.conf = self.read_config_file(config_file_location)

    def read_config_file(self, config_file):
        """Read Confluent Cloud configuration for librdkafka clients"""
        conf = {}
        with open(config_file) as fh:
            for line in fh:
                line = line.strip()
                if len(line) != 0 and line[0] != "#":
                    parameter, value = line.strip().split('=', 1)
                    conf[parameter] = value.strip()
        conf['ssl.ca.location'] = certifi.where()
        return conf

    def pop_schema_registry_params_from_config(self):
        """Remove potential Schema Registry related configurations from dictionary"""
        self.conf.pop('schema.registry.url', None)
        self.conf.pop('basic.auth.user.info', None)
        self.conf.pop('basic.auth.credentials.source', None)
        self.conf.pop('session.timeout.ms', None)
        return self.conf

    def consume_date(self, topic, *args, **kwargs):
        # Subscribe to topic
        consumer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
        consumer_conf['auto.offset.reset'] = 'earliest'
        consumer = Consumer(consumer_conf)
        consumer.subscribe([topic])