# cd /home/github/confluent_kafka/
# /root/.virtualenvs/confluent_kafka-uEDxVY-e/bin/python producer_python.py -f "data/episode.json"

from KafkaProducerClass import KafkaProducer
import json
import itertools
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-file', type=str)
args = parser.parse_args()

#topic_name = "episode"
#process_file = "data/title.crew.json"
topic_regex_match = re.search("(?<=data/json/)(.*)(?=.json)", args.file)
topic_name = topic_regex_match.group() if topic_regex_match else ""
process_file = args.file
print(f"Processing {args.file}")

# Instantiate KafkaProducer
kafka = KafkaProducer(config_file_location="python.config")


# Create Generator Function to pull large Json Data
def gen_json(file_name):
    with open(file_name) as fh:
        while line := fh.readline():
            yield json.loads(line)


if __name__ == "__main__":

    # Create Kafka Topic
    kafka.create_topic(topic_name, num_partitions=2, replication_factor=3)

    # Pull the first 10000 rows from the generator
    top10000 = tuple(itertools.islice(gen_json(process_file), 10000))

    # Send data to Kafka
    for message in top10000[0]:

        kafka.produce_data(
            topic_name,
            key=str(top10000[0].index(message)),
            value=json.dumps(message)
        )
