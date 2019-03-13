import requests
import time
from tokens import token_group

r2 = requests.get('https://api.vk.com/method/groups.getLongPollServer?',
                  params={'group_id': '179378864',
                          'access_token': token_group,
                          'v': '5.92'})

print(r2)
print(r2.text)
print(r2.json())

serv = r2.json()['response']['server']
key = r2.json()['response']['key']
ts = r2.json()['response']['ts']

serv += '?'

print(serv, ts)

while 5 < 10:
    r3 = requests.get(serv, params={'act': 'a_check', 'key': key, 'ts': ts})
    print(r3.json())
    if 'updates' in r3.json():
        l = list(r3.json()['updates'])
        for d in l:
            if 'object' in d:
                print('Победа')
                if 'from_id' in d['object']:
                    r = requests.get('https://api.vk.com/method/users.get?',
                                     params={'access_token': token_group,
                                    'v': '5.92',
                                    'user_ids': d['object']['from_id']})
                    print(r.json())
                    r = requests.get('https://api.vk.com/method/messages.send?',
                                     params={'user_id': d['object']['from_id'],
                                             'random_id': 0,
                                             'message': 'Привет',
                                             'group_id': '179378864',
                                             'access_token': token_group,
                                             'v': '5.92',
                                             })
                    print(r)
                    print(r.text)
    ts = r3.json()['ts']
    time.sleep(10)




