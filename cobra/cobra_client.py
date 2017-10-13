import requests
import json

question = requests.get('http://127.0.0.1:8000/getquestion')
data = json.loads(question.text)

print('''\
{title}
{text}
{signature}
'''.format(**data))

solution = ''
user_input = None
while user_input != '':
    user_input = input()
    solution += user_input + '\n'
    
print(solution)

print('Now the solution should run and with the unittests')
print(data['unittests'])