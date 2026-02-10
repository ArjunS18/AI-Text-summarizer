from clients.bedrock_client import BedrockClient
from utils.prompt_builder import build_prompt
from utils.decorators import timing_decorator, exception_handler, log_request


bedrock_client = BedrockClient()


@exception_handler
@timing_decorator
@log_request
def summarize_text(request_model):
    """
    Main summarization service logic.
    """

    prompt = build_prompt(
        text=request_model.text,
        summary_type=request_model.summary_type
    )

    summary = bedrock_client.invoke_model(
        prompt=prompt,
        max_tokens=request_model.max_tokens,
        temperature=request_model.temperature,
        top_p=request_model.top_p
    )

    return summary
