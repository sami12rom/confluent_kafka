topic_name="essent_knowledge_booth_rest_api"

# Create Kafka Topic using the Confluent Cloud REST API

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic UFNXM0xTQVZQMjNUVFQ3STpHRzBHU2Z3bGlPVUpMc3dacCtzRkxRQ1EyTXFzUFRYY3B5L2JuWmtkdFNFMmRpeTFCZFJsTnBQYU8wVCs1cFRM" \
  https://pkc-zpjg0.eu-central-1.aws.confluent.cloud:443/kafka/v3/clusters/lkc-zmvn3y/topics \
  -d '{"topic_name":"'"$topic_name"'"}'


# Produce records using the Confluent Cloud REST API 
# Non-Streaming Mode
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic UFNXM0xTQVZQMjNUVFQ3STpHRzBHU2Z3bGlPVUpMc3dacCtzRkxRQ1EyTXFzUFRYY3B5L2JuWmtkdFNFMmRpeTFCZFJsTnBQYU8wVCs1cFRM" \
  https://pkc-zpjg0.eu-central-1.aws.confluent.cloud:443/kafka/v3/clusters/lkc-zmvn3y/topics/$topic_name/records \
  -d '{"value":{"type":"JSON","data":"Hello World!"}}'

# Produce records using the Confluent Cloud REST API 
# Streaming Mode
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Transfer-Encoding: chunked" \
  -H "Authorization: Basic UFNXM0xTQVZQMjNUVFQ3STpHRzBHU2Z3bGlPVUpMc3dacCtzRkxRQ1EyTXFzUFRYY3B5L2JuWmtkdFNFMmRpeTFCZFJsTnBQYU8wVCs1cFRM" \
  https://pkc-zpjg0.eu-central-1.aws.confluent.cloud:443/kafka/v3/clusters/lkc-zmvn3y/topics/$topic_name/records \
  -T-
  