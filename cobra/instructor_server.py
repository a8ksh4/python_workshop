import falcon
import yaml
from random import *
import uuid
import json

def load_yaml(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.load(f.read())
    return data

    
class QuestionResource():
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        question_id = '4464b29f-86a1-4e4c-9261-f581d1b1c8e8'    # this will be pulled from somewhere else
        title = data[question_id]['title']
        text = data[question_id]['text']
        signature = data[question_id]['signature']
        tags = data[question_id]['tags']
        unittests = data[question_id]['unittests']
        imports = data[question_id]['imports']
        setup = data[question_id]['setup']
        teardown = data[question_id]['teardown']
        token = str(uuid.uuid4())    # this will probably be from a user database or something, once multiuser is worked out.
        body = {'title': title, 
                'text': text, 
                'signature': signature, 
                'tags': tags, 
                'unittests': unittests, 
                'setup': setup, 
                'teardown': teardown,
                'imports': imports,
                'token': token}
        resp.body = (json.dumps(body))

   
        
data = load_yaml('format_example.yml')
app = falcon.API()
instructions = QuestionResource()
app.add_route('/getquestion', instructions)

