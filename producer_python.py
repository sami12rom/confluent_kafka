from KafkaProducerClass import KafkaProducer
import json

topic_name = "essent_knowledge_booth_python"

# Instantiate KafkaProducer
kafka = KafkaProducer(config_file_location="python.config")

# Create Kafka Topic
kafka.create_topic(topic_name, num_partitions=3, replication_factor=3)

kafka.produce_data(
    topic,
    key=record_key,
    value=json.dumps(record_value),
    headers=metadata
)
