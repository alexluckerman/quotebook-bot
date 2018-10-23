import requests
import re

endpoint = 'https://api.groupme.com/v3'
token = {
    'token' : '',
}
group_id = ''
single_quote_rule = re.compile(r'["“”].+["“”] - ?.+')
multi_quote_rule = re.compile(r'(.+: ["“”].+["“”])*\n(.+: ["“”].+["“”])+')

response_text_list = [
    "Hey, you're getting this message because you posted something that's not a properly formatted quote in the Quote Book.", 
    "Here's a few examples of properly formatted quotes:",
    "\"Something dumb\" - person",
    "\"other dumb stuff\" -Person",
    "Person 1: \"Some dumb stuff\"\nPerson 2: \"Other dumb stuff\"",
    "And here's a link to join the Quote Book Discussion, where you can post any responses to quotes that get posted in the main group: https://link-to-discussion-group.com"
]

msg_extension = '/groups' + group_id + '/messages'
dm_extension = '/direct_messages'

# Gets most recent quote, checks it for proper formatting, and DMs the poster if the formatting is wrong
def process_quote():
    resp = requests.get(endpoint + msg_extension, params=token)
    print(resp.url)
    print(resp.status_code)
    last_msg = resp.json()['response']['messages'][0]
    print(last_msg)
    if last_msg['system'] == True:
        return
    last_msg_user = last_msg['user_id']
    last_msg_text = last_msg['text']
    if single_quote_rule.match(last_msg_text) or multi_quote_rule.match(last_msg_text):
        return
    iter = 0
    for response_text in response_text_list:
        iter = iter + 1
        payload = {
            'direct_message': {
                'source_guid': 'Message ' + str(iter),
                "recipient_id": last_msg_user,
                "text": response_text
            }
        }
        resp = requests.post(endpoint + dm_extension, params=token, json=payload)
        print(resp.url)
        print(resp.status_code)

process_quote()