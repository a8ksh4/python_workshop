import falcon
import yaml
from random import *
import uuid
import json
from utility import decode_message, encode_message
from server_utility import Questions, Users, User

class GetLessons():
    def on_get(self, req, resp):
         resp.body = json.dumps(questions.get_lessons())
         
class GetQuestions():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        lesson = post_info['lesson']
        resp.body = json.dumps(questions.get_questions(lesson))
        
class GetQuestion():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        username = post_info['username']
        lesson = post_info['lesson']
        question_label = post_info['question_label']
        seed = users.users[username].new_seed()
        question = questions.get_question(lesson, question_label)
        question.pop('solution')
        question.pop('history')
        question.update({'seed':seed})
        resp.body = json.dumps(question)
        
        
        
"""
class GetQuestion():
    def on_get(self, req, resp):
        '''Handles GET requests'''
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
        pretest = data[question_id]['pretest']
        posttest = data[question_id]['posttest'] 
        token = str(uuid.uuid4())    # this will probably be from a user database or something, once multiuser is worked out.
        seed = 323423                # this will eventually be randomized per session
        body = {'id': question_id,
                'title': title, 
                'text': text, 
                'signature': signature, 
                'tags': tags, 
                'unittests': unittests, 
                'setup': setup, 
                'teardown': teardown,
                'pretest': pretest,
                'posttest': posttest,
                'imports': imports,
                'token': token,
                'seed': seed}
        
        #body = data[question_id]
        #body['seed'] = 215646
        #body.pop('solution')
        #body.pop('history')
        
        resp.body = (json.dumps(body))
"""
        
        
class AddUser():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        ip = req.remote_addr
        username = post_info['username']
        password = post_info['password']
        users.users.update({username: User(username)})
        if users.users[username].create_user(decode_message(password), ip):
            sessionid = users.users[username].create_new_session()
        else:
            raise
        resp.body = sessionid
       
class LoginUser():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        ip = req.remote_addr
        username = post_info['username']        
        password = post_info['password']
        if users.users[username].login_user(password, ip):
            sessionid = users.users[username].create_new_session()
        else:
            raise
        resp.body = sessionid
        
class SubmitSoltion():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        ip = req.remote_addr
        solution = post_info['solution']
        print(solution)
        #resp.body = 

questions = Questions()
users = Users()
app = falcon.API()
app.add_route('/getlessons', GetLessons())
app.add_route('/getquestions', GetQuestions())
app.add_route('/getquestion', GetQuestion())
app.add_route('/newuser', AddUser())
app.add_route('/login', LoginUser())

