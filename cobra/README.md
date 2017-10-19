# to run the server
```
pip install gunicorn
gunicorn instructor_server:app
```
or
```
pip install waitress
waitress-serve --port=8000 instructor_server:app
```

# required modules:
```
conda install prompt_toolkit
pip install ptpython
conda install flake8
```

