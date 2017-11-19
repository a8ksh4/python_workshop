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
All of the student problems start out in doctest format.  See the "problems.py" in each of the content directories above the cobra directory.  E.g. 3-files_and_paths/problems.py.  Starting with doctest lets us validate all of our problems and the test cases in an easy-to-use format before we port them to the format needed for the client-server tool.  Then we run a translate tool and a validate tool to get them into yml format to use.

1. Create problems.py in doctest format.
2. Run problems.py and verify no doctest errors.
3. Translate the problem to yml format:
  * The format is "translate_doctest.py <source doctest file> <dest yml file>":
  * `./translate_doctest.py ../3-files_and_paths/problems.py ./enabled/3_problems.yml`
4. **Validate** the ouptut yml file:
  This will iterate over all of the problesm in teh file and 
  execute them the same way that they would be run when a user 
  submits a solution.  It will halt on any errors if found, and
  you can re-work the doctest version of the problem, translate
  again, and re-run validate.  
  * The format is "validate_yml.py <yml file path>"
  * `./validate_yml.py ./enabled/3_problems.yml`
