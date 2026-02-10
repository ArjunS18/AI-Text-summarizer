def build_prompt(text, summary_type):

    if summary_type == "concise":
        instruction = "Summarize the following text in 3-5 clear sentences."
    elif summary_type == "detailed":
        instruction = "Provide a detailed summary including key insights and explanations."
    elif summary_type == "bullet_points":
        instruction = "Summarize the text into structured bullet points."
    else:
        instruction = "Summarize the text clearly."

    prompt = f""" You are a professional AI assistant.
{instruction}
Text:
{text}
Return only the summary.
"""

    return prompt.strip()
