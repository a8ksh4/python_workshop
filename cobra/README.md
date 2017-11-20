# Starting the Server
**Install required modules**
```
conda install prompt_toolkit
pip install ptpython
conda install flake8
```
**In Linux**
```
pip install gunicorn
cd python_class/cobra
./run_gunicorn_server.sh
```
**In Windows**
```
pip install waitress
run_waitress_server.bat
```
  
# Running the client
Students update the bottom of the **cobra_client.py** file with the IP of the class server and port:
```python
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
```
  
# Creating Content
A video demo of this is hosted here:  
[![test](https://img.youtube.com/vi/fzwtEEb42D0/hqdefault.jpg)](https://www.youtube.com/watch?v=fzwtEEb42D0)  
  
All of the student problems start out in doctest format.  See the "problems.py" in each of the content directories above the cobra directory.  E.g. 3-files_and_paths/problems.py.  Starting with doctest lets us validate all of our problems and the test cases in an easy-to-use format before we port them to the format needed for the client-server tool.  Then we run a translate tool and a validate tool to get them into yml format to use.

1. **Create problems.py in doctest format**.  
  Follow the format of the example files closely.  
  * imports and \_helper functions go at the top of the file.
    These are executed at the start of every problem to set
    up the environment for it.  
  * Problem functions All have a name (function name), arguments 
    defined, an example solutoin in the body of the function,
    and a doc-string that contains all of the description and
    validation code for the problem.  
    * First line of the docstring is a problem title - not super 
      important, but the line must be present. 
    * Next few lines are a description of the problem that the
      user sees that explains the requirements clearly to them. 
    * Next is the doctest content that is used to validate that
      a given solution is correct.  Any line in this section
      that is followed by "True" on the next line will be used
      to validate the problem once it is translated to yml
      format for the student tool.  I was fairly careful to
      craft these to get specific output and have a condition
      I want to check result in True being returned. 
  * Next,the solution to the problem is given.  
  * Finally is the return statement.  Keep any code to generate
    the return value on a separate line and only return
    a descriptive variable or "# return nothing".  This line is
    used to generate the description of the problem for the user
    tool so needs to follow these requirements. 
2. **Run problems.py and verify no doctest errors**.  
3. **Translate the problem to yml format**:  
 * The format is "translate_doctest.py <source doctest file> <dest yml file>":
 * `./translate_doctest.py ../3-files_and_paths/problems.py ./enabled/3_problems.yml`
4. **Validate the ouptut yml file**:  
  This will iterate over all of the problesm in teh file and 
  execute them the same way that they would be run when a user 
  submits a solution.  It will halt on any errors if found, and
  you can re-work the doctest version of the problem, translate
  again, and re-run validate.  
  * The format is "validate_yml.py <yml file path>"
  * `./validate_yml.py ./enabled/3_problems.yml`
5. **Add completed problems to question_list.yml**  
  These are the problems that will be delivered to the user when they run the 
  tool during class. Format is like [file name without extension, problem_name]:
```
$ cat question_list.yml 
- [2_problems, addThem]
- [2_problems, carmenFound]
...
```
