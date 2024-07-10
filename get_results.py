from gpt_model import ChatCompletionClient
from utils.prompts import SYSTEM_PROMPT, USER_PROMPT, N_SHOT_SYSTEM_PROMPT
import json
from typing import List, Dict, Any

GPT_35_TURBO = ChatCompletionClient(SYSTEM_PROMPT, "gpt-3.5-turbo")
GPT_4_TURBO = ChatCompletionClient(SYSTEM_PROMPT, "gpt-4-turbo-preview")

def get_result_gpt3(record: Any) -> List[Dict[str, Any]]:
    """
    Get results from GPT-3.5 turbo model for each claim in the record.

    Args:
        record (Any): The record containing claims and content.

    Returns:
        List[Dict[str, Any]]: A list of results for each claim.
    """
    result = []
    for claim in record.claims:
        try:
            user = USER_PROMPT.format_map({'claim': claim, 'content': record.content})
            completion = GPT_35_TURBO.get_response(user)
            instances = json.loads(completion.choices[0].message.content)
            result.append({'claim': claim, 'instances': instances, 'raw_instances': completion.choices[0].message.content})
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for claim '{claim}': {e}")
        except Exception as e:
            print(f"Error processing claim '{claim}': {e}")
    return result

def get_result_gpt4(record: Any) -> List[Dict[str, Any]]:
    """
    Get results from GPT-4 turbo model for each claim in the record.

    Args:
        record (Any): The record containing claims and content.

    Returns:
        List[Dict[str, Any]]: A list of results for each claim.
    """
    result = []
    for claim in record.claims:
        try:
            user = USER_PROMPT.format_map({'claim': claim, 'content': record.content})
            completion = GPT_4_TURBO.get_response(user)
            instances = json.loads(completion.choices[0].message.content)
            result.append({'claim': claim, 'instances': instances, 'raw_instances': completion.choices[0].message.content})
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for claim '{claim}': {e}")
        except Exception as e:
            print(f"Error processing claim '{claim}': {e}")
    return result

def get_result_nshot(record: Any, examples: str) -> List[Dict[str, Any]]:
    """
    Get n-shot results from GPT-3.5 turbo model for each claim in the record using provided examples.

    Args:
        record (Any): The record containing claims and content.
        examples (str): The examples to be used for n-shot learning.

    Returns:
        List[Dict[str, Any]]: A list of results for each claim.
    """
    result = []
    GPT_35_TURBO_NSHOT = ChatCompletionClient(N_SHOT_SYSTEM_PROMPT.format(examples= examples), "gpt-3.5-turbo")
    for claim in record.claims:
        try:
            user = USER_PROMPT.format_map({'claim': claim, 'content': record.content})
            completion = GPT_35_TURBO_NSHOT.get_response(user)
            instances = json.loads(completion.choices[0].message.content)
            result.append({'claim': claim, 'instances': instances, 'raw_instances': completion.choices[0].message.content})
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for claim '{claim}': {e}")
        except Exception as e:
            print(f"Error processing claim '{claim}': {e}")
    return result