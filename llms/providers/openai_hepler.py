import os
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI
from langchain_openai import AzureChatOpenAI, AzureOpenAI

logger = logging.getLogger("logger")


def initialize_ai_client(model="gpt-3.5-turbo", use_chat_client=True):
    """
    Initializes and returns an AI client based on environment configuration and client type.

    Args:
        use_chat_client (bool): If True, initializes a chat-specific client (e.g., ChatOpenAI or AzureChatOpenAI).
                                If False, initializes a general client (e.g., OpenAI or AzureOpenAI).

    Returns:
        An instance of either OpenAI, ChatOpenAI, AzureOpenAI, or AzureChatOpenAI based on the environment settings
        and the 'use_chat_client' flag.

    Raises:
        ValueError: If the required API keys are not found in the environment variables.
    """
    # Check if Azure OpenAI key and endpoint are available
    azure_api_key = os.getenv('AZURE_OPENAI_API_KEY')
    azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

    if azure_api_key and azure_endpoint:
        # logger.info("Initializing Azure OpenAI client...")
        params = {
            "model":  os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
            "deployment_name":  os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
        }
        if use_chat_client:
            return AzureChatOpenAI(**params)
        else:
            return AzureOpenAI(**params)
    else:
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OpenAI API key not found in environment variables.")
        # logger.info(f"Initializing OpenAI {model} client...")
        if use_chat_client:
            return ChatOpenAI(model=model, api_key=openai_api_key)
        else:
            return OpenAI(model=model, api_key=openai_api_key)

if __name__ == "__main__":
    load_dotenv("./.env", verbose=True)
    client = initialize_ai_client(use_chat_client=True)

    res = client.invoke(["hi, i'm bob"])
    res.pretty_print()
    print(res.response_metadata)

