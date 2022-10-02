import sys
from confluent_kafka.admin import AdminClient, NewTopic  # noqa: E402
import certifi  # noqa: E402
from confluent_kafka import Producer, KafkaError  # noqa: E402


class KafkaProducer:
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

    def create_topic(self, topic, num_partitions=1, *args, **kwargs):
        """Create Topic if needed"""
        admin_client_conf = self.pop_schema_registry_params_from_config()
        admin = AdminClient(admin_client_conf)
        fs = admin.create_topics([NewTopic(topic, num_partitions=num_partitions, *args, **kwargs)])
        try:
            fs[topic].result()
            print(f"Topic {topic} created")
        except Exception as e:
            if e.args[0].code() == KafkaError.TOPIC_ALREADY_EXISTS:
                print(f"Result to create topic {topic}: {e}")
            else:
                print(f"Failed to create topic {topic}: {e}")
                sys.exit(1)
    
    def list_topics(self, topic=None):
        admin_client_conf = self.pop_schema_registry_params_from_config()
        admin = AdminClient(admin_client_conf)
        fs = admin.list_topics(topic)
        return fs



    def acknowledge_delivery(self, err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        Optional per-message on_delivery handler (triggered by poll() or flush()
        """
        if err is not None:
            print(f"Failed to deliver message: {err}")
        else:
            print(f"Produced record to topic {msg.topic()}, partition [{msg.partition()}] @ offset {msg.offset()}")

    def produce_data(self, topic, key, value, *args, **kwargs):
        """Produce data to Confluent"""
        producer = Producer(self.pop_schema_registry_params_from_config())
        try:
            producer.produce(topic, key=key, value=value, on_delivery=self.acknowledge_delivery, *args, **kwargs)
            producer.poll(0)
            producer.flush()
            # print(f"Messages were produced to topic {topic}!")
        except Exception as e:
            print(e)
            sys.exit(1)
