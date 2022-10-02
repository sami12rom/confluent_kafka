topic_name="trial1"
api_key="_"
api_secret="_"
# Create base64 authorization and remove unnecessary characters
authorization=$(echo "$api_key:$api_secret" | base64 | tr "/+" "_-" | tr -d "="| tr -d "\n")


# Create Kafka Topic using the Confluent Cloud REST API
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic $authorization" \
  https://pkc-zpjg0.eu-central-1.aws.confluent.cloud:443/kafka/v3/clusters/lkc-7yxmwp/topics \
  -d '{"topic_name":"'"$topic_name"'"}'

# Produce records using the Confluent Cloud REST API 
# Non-Streaming Mode
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic $authorization" \
   https://pkc-zpjg0.eu-central-1.aws.confluent.cloud:443/kafka/v3/clusters/lkc-7yxmwp/topics/$topic_name/records \
  -d '{"value":{"type":"JSON","data":"Hello World!"}}'


# Produce records using the Confluent Cloud REST API 
# Streaming Mode
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Transfer-Encoding: chunked" \
  -H "Authorization: Basic $authorization" \
  https://pkc-zpjg0.eu-central-1.aws.confluent.cloud:443/kafka/v3/clusters/lkc-gqd3g1/topics/$topic_name/records \
  -T-
  