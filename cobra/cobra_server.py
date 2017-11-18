import falcon
import yaml
#from random import *
#import uuid
import json
from util.utility import decode_message, encode_message, hash_results, load_yml
from util.server_utility import Questions, User, get_users, update_history, get_history
from util.solution_checker import Solution


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
        seed = users[username].new_seed()
        question = questions.get_question(lesson, question_label)
        question.pop('solution')
        #question.pop('history')
        question.update({'seed':seed})
        resp.body = json.dumps(question)
        
class AddUser():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        ip = req.remote_addr
        username = post_info['username']
        password = decode_message(post_info['password'])
        users.update({username: User(username)})
        if users[username].create_user(password, ip):
            sessionid = users[username].create_new_session()
        else:
            raise
        resp.body = encode_message(sessionid)
       
class LoginUser():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        ip = req.remote_addr
        username = post_info['username']        
        password = decode_message(post_info['password'])
        sessionid = decode_message(post_info['sessionid'])
        login_pass = False
        
        if users[username].check_session_id(sessionid, ip):
            login_pass = True
        elif users[username].login_user(password, ip):
            login_pass = True
        else:
            sessionid = '-1'
        if login_pass:
            sessionid = users[username].create_new_session()
        resp.body = encode_message(sessionid)
        
class SubmitSolution():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        ip = req.remote_addr
        username = post_info['username']
        lesson = post_info['lesson']
        question_label = post_info['question_label']
        solution = post_info['solution']
        submitted_results = post_info['results']
        stats = post_info['stats']
        question = questions.get_question(lesson, question_label)
        question.update({'seed': users[username].get_seed()})
        master_results = Solution(question)
        master_results.run_solution()
        print(master_results.test_results)
        print(submitted_results)
        if hash_results(master_results.test_results) == submitted_results:
            correct = [lesson, question_label]
            users[username].update_completed(correct)
            update_history(correct, username, solution, stats)
        else:
            correct = 'fail'
        resp.body = json.dumps(correct)
        
class GetNextQuestion():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        response = [None, None]
        question_list = load_yml('question_list.yml')
        username = post_info['username']
        for lesson, question_label in question_list:
            if [lesson, question_label] in users[username].get_completed():
                continue
            else:
                response = [lesson, question_label]
                break
        resp.body = json.dumps(response)
        
class GetHistory():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        lesson = post_info['lesson']
        question_label = post_info['question_label']
        username = post_info['username']
        question_item = [lesson, question_label]
        if question_item in users[username].get_completed():
            history = get_history(question_item)
            if history:
                pass
            else:
                history = {}
        else:
            history = {}
        resp.body = json.dumps(history)

class GetCompleted():
    def on_post(self, req, resp):
        post_info = json.loads(req.stream.read().decode('utf-8'))
        username = post_info['username']
        completed = users[username].get_completed()
        resp.body = json.dumps(completed)
        
questions = Questions()
users = get_users()
app = falcon.API()
app.add_route('/getlessons', GetLessons())
app.add_route('/getquestions', GetQuestions())
app.add_route('/getquestion', GetQuestion())
app.add_route('/newuser', AddUser())
app.add_route('/login', LoginUser())
app.add_route('/submitsolution', SubmitSolution())
app.add_route('/getnextquestion', GetNextQuestion())
app.add_route('/gethistory', GetHistory())
app.add_route('/getcompleted', GetCompleted())
