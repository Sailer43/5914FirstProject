import json
import ibm_watson

service = ibm_watson.AssistantV2(
    version='development',
    iam_apikey='A4LMwqnkIQac81v88v14_AZLj5F__wjY83S9WOgjqAXw',
    url='https://gateway-wdc.watsonplatform.net/assistant/api'
)

response = service.create_session(
    assistant_id='f2ddf51f-1048-44ad-a4a8-3d5a5289178a',
    session_id='{session_id}',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))
