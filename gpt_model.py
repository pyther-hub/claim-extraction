from dotenv import load_dotenv
from openai import OpenAI
from typing import Dict

load_dotenv()

class ChatCompletionClient:
    client: OpenAI = OpenAI()

    def __init__(self, system_prompt: str, model_name: str = "gpt-3.5-turbo") -> None:
        """
        Initialize the ChatCompletionClient.

        Args:
            system_prompt (str): The system prompt used for chat completions.
            model_name (str, optional): The name of the OpenAI model to use. Defaults to "gpt-3.5-turbo".
        """
        self.system_prompt = system_prompt
        self.model_name = model_name

    def get_response(self, user_message: str) -> Dict[str, any]:
        """
        Get response from OpenAI chat completion API.

        Args:
            user_message (str): The message from the user.

        Returns:
            Dict[str, any]: The completion response from OpenAI.
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.0
            )
            return completion
        except Exception as e:
            print(f"Error in get_response: {e}")
            return {}
