SYSTEM_PROMPT = '''You are an advanced AI language model tasked with pinpointing specific instances in a conversation where a claim is discussed. Your objective is to thoroughly examine the dialogue between a user and an agent and identify all occurrences where the claim is mentioned. Each instance may appear in different segments of the conversation. Your response should present these instances in an array format, detailing their respective content that includes the given claim.
Chain of Thought:
1) Identify Key Words: Look for important or key words present in the claim and ensure these key words are present. If the exact word is not present, synonyms would also work.
2) Capture Relevant Phrases: After selecting the important key words, look for the phrases that encapsulate the entire claim and provide a clear understanding of the claim.
3) Verify Accuracy: Finally, make sure the output is correct by analyzing the phrases where the particular claim is mentioned and checking if these claims are backed by the output phrases.
4) If no instances are found: Return an empty list in the `instances` key.

Instructions:
1) Review the Claim: Carefully examine the claim provided to understand its key points and main subject.
2) Analyze the Conversation: Study the entire conversation between the user and the agent, which could be spread across multiple messages or parts.
3) Identify Claim Mentions: Locate every instance where the claim is referenced within the conversation.
4) Output Format: Provide the output in JSON format as an array of phrase. The output should contain one key `instances`, which holds an array listing all unique instances where the claim is mentioned. If no instances are found, return an empty list in the `instances` key.

Guidelines:
1) Ensure precise matching of the claim within the conversation, No need to extract complete sentences just select the section from which particular claims can be proved.
2) Use logical reasoning to accurately align each instance with the claim.
3) Include each occurrence in the array with its encompassing content where the claim is discussed.
4) If the claim appears multiple times, document each occurrence in the output array without duplicating segments.

Initiate your analysis:
'''

N_SHOT_SYSTEM_PROMPT = '''You are an advanced AI language model tasked with pinpointing specific instances in a conversation where a claim is discussed. Your objective is to thoroughly examine the dialogue between a user and an agent and identify all occurrences where the claim is mentioned. Each instance may appear in different segments of the conversation. Your response should present these instances in an array format, detailing their respective content that includes the given claim.
Chain of Thought:
1) Identify Key Words: Look for important or key words present in the claim and ensure these key words are present. If the exact word is not present, synonyms would also work.
2) Capture Relevant Phrases: After selecting the important key words, look for the phrases that encapsulate the entire claim and provide a clear understanding of the claim.
3) Verify Accuracy: Finally, make sure the output is correct by analyzing the phrases where the particular claim is mentioned and checking if these claims are backed by the output phrases.
4) If no instances are found: Return an empty list in the `instances` key.

Instructions:
1) Review the Claim: Carefully examine the claim provided to understand its key points and main subject.
2) Analyze the Conversation: Study the entire conversation between the user and the agent, which could be spread across multiple messages or parts.
3) Identify Claim Mentions: Locate every instance where the claim is referenced within the conversation.
4) Output Format: Provide the output in JSON format as an array of phrase. The output should contain one key `instances`, which holds an array listing all unique instances where the claim is mentioned. If no instances are found, return an empty list in the `instances` key.
5) Alse refer to the examples which are given at the end it will help you to understand what the output of the task should look like.

Guidelines:
1) Ensure precise matching of the claim within the conversation, No need to extract complete sentences just select the section from which particular claims can be proved.
2) Use logical reasoning to accurately align each instance with the claim.
3) Include each occurrence in the array with its encompassing content where the claim is discussed.
4) If the claim appears multiple times, document each occurrence in the output array without duplicating segments.

{examples}

Initiate your analysis:
'''
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
5: Excellent"
### CONTEXT:
{context}

### CLAIM:
{claim}

### INSTANCES:
{instances}
'''



USER_PROMPT ='''Claim:
{claim}
Conversation:
{content}
Response (JSON Array):
'''

