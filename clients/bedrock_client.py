import boto3
import json
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

region = os.getenv("AWS_REGION")

class BedrockClient:

    def __init__(self):
        self.region = os.getenv("AWS_REGION", "us-west-2")
        self.model_id = os.getenv(
            "BEDROCK_MODEL_ID",
            "amazon.nova-micro-v1:0"
        )

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=self.region
        )

    def invoke_model(self, prompt, max_tokens, temperature, top_p) -> str:
        """
        Sends request to Amazon Bedrock and returns generated text.
        """

        client = boto3.client(
            "bedrock-runtime",
            region_name="us-west-2"
        )


        messages = [
            {"role": "user", "content": [{"text": prompt}]},
        ]

        inf_params = {"maxTokens": max_tokens, "topP": top_p, "temperature": temperature}

        additionalModelRequestFields = {
            "inferenceConfig": {
                "topK": 20
            }
        }

        model_response = client.converse(
            modelId="us.amazon.nova-lite-v1:0",
            messages=messages,
            inferenceConfig=inf_params,
            additionalModelRequestFields=additionalModelRequestFields
        )

        print("\n[Full Response]")
        print(json.dumps(model_response, indent=2))

        print("\n[Response Content Text]")
        print(model_response["output"]["message"]["content"][0]["text"])

        summary_text = json.dumps(model_response["output"]["message"]["content"][0]["text"])

        return summary_text.strip()
