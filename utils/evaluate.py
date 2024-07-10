from ..gpt_model import ChatCompletionClient
from utils.prompts import SYSTEM_PROMPT, USER_PROMPT, N_SHOT_SYSTEM_PROMPT
import json
from typing import List, Dict, Any

GPT_35_TURBO = ChatCompletionClient(SYSTEM_PROMPT, "gpt-3.5-turbo")
GPT_4_TURBO = ChatCompletionClient(SYSTEM_PROMPT, "gpt-4-turbo-preview")

EVALUATION_OF_RESULT_SYSTEM_PROMPT = '''Evaluate the relevance of the extracted phrases from the given conversation between an agent and a user. You will also be given a specific claim. Assess strictly based on instances drawn directly from the conversation:

Evaluation should be strictly based on the instances.
1) Rate how well these instances support the claim; their relevance to the claim is crucial.
2) Instances are already extracted; you have to rate how well these instances fulfill the claim.
3) Provide a rating between 0 and 5 to indicate the relevance of the claim to the conversation. Use the following scale:

Begin with an explanation for your response. End with a single integer rating from the provided scale.

0: Extremely irrelevant
1: Very bad
2: Bad
3: Good
4: Very good
5: Excellent

Output Format: Your output should be a JSON file with two keys:
- "explanation": Explanation of your response.
- "score": Single integer rating from 0 to 5 indicating the relevance.
'''

EVALUATION_USER_PROMPT = '''### CONTEXT:
{context}

### CLAIM:
{claim}

### INSTANCES:
{instances}
'''

GPT_35_TURBO = ChatCompletionClient(EVALUATION_OF_RESULT_SYSTEM_PROMPT, "gpt-3.5-turbo")

def evaluate_the_record(record: Any) -> List[Dict[str, Any]]:
    """
    Evaluates a single record by generating a response using a GPT model.

    Args:
        record (Any): The record containing the context, claim, and instances to be evaluated.

    Returns:
        List[Dict[str, Any]]: A list of evaluation results with explanations and scores.
    """
    results = []
    for row in record.instances:
        try:
            eval_prompt = EVALUATION_USER_PROMPT.format(
                context=record.content,
                claim=row['claim'],
                instances=' '.join(row['instances']['instances'])
            )
            res = GPT_35_TURBO.get_response(eval_prompt)
            res_content = json.loads(res.choices[0].message.content)
            results.append(res_content)
        except Exception as e:
            print(f"Error evaluating row {row}: {e}")
            results.append({"explanation": "Error processing this instance.", "score": 0})
    return results
    
def evaluate_all_the_records(records: List[Any]) -> List[Dict[str, Any]]:
    """
    Evaluates multiple records by iterating through each and generating responses using a GPT model.

    Args:
        records (List[Any]): A list of records to be evaluated.

    Returns:
        List[Dict[str, Any]]: A combined list of evaluation results for all records.
    """
    results = []
    for record in records:
        results += evaluate_the_record(record)
    return results
