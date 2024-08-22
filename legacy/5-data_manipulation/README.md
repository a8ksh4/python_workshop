# Index:
* [csv](#csv)
* [json](#json-module)
* [yaml](#yaml-module)
* [regex](#re-module)
* [sql and sqlite](#sql-and-sqlite)
  
# csv
CSV format is simple to parse manually and the csv module is simple to use.  CSV doesn't scale well
when lots of parameters are needed, like in a config file, but it's an ubiquitous, simple, format 
since exceldocs can be exported to it.  
  
**Parsing csv manually**  
```python
my_file = './foo.csv'
my_data = []
with open(my_file, 'r') as f:
    for line in f.readlines():
        line = line.strip().split(',')
        my_data.append(line)
```
  
**And wirting it manually**  
```python
new_file = './foo_out.csv'
my_data = [ [1, 2, 3, 4], ['a', 'b', 'c', 'd'], [7, 8, 9, 10] ]
with open(new_file, 'w') as f:
    for line in my_data:
        line = ','.join(line)
        f.write(line + '\n')
```
  
**Reading with csv module**  
```python
import csv
my_file = './foo.csv'
my_data = []
with open(my_file, 'r') as f:
    csv_reader = csv.reader(f, delimteter=':', quotechar='|', ...)
```
  
**Writing with csv module**  
    

# json modulel
Json looks a lot like python code. It's "JavaScript Object Notation", a scheme for encapsulating data
that's way easier to read/write than xml.

**json.dumps**
json.dumps returns a string encoded as json, representing the data passed to it.  
```python
In [30]: mod_cfg
Out[30]: 
[{'directive': 'install', 'name': 'module1'},
 {'directive': 'remove', 'name': 'module2'},
 {'directive': 'tbd', 'name': 'foobar'}]

In [36]: json_str = json.dumps(mod_cfg)

In [37]: print json_str
[{"name": "module1", "directive": "install"}, {"name": "module2", "directive": "remove"}, {"name": "foobar", "directive": "tbd"}]
```

**json.dump**  
Similar to json.dumps, but used for writing to a file.  
```python
In [33]: with open('modules.json', 'w') as f:
    ...:     json.dump(mod_cfg, f)
    ...:     

In [35]: open('modules.json', 'r').read()
Out[35]: '[{"name": "module1", "directive": "install"}, {"name": "module2", "directive": "remove"}, {"name": "foobar", "directive": "tbd"}]'
```
  
**json.loads**  
Loads json data from a string.  
```python
In [39]: mod_cfg = json.loads(json_str)

In [40]: print mod_cfg
[{u'name': u'module1', u'directive': u'install'}, {u'name': u'module2', u'directive': u'remove'}, {u'name': u'foobar', u'directive': u'tbd'}]
```
  
**json.load**  
Similar, for reading json data from a file.  
```python
In [42]: with open('modules.json', 'r') as f:
    ...:     mod_cfg = json.load(f)
    ...:     

In [43]: print mod_cfg
[{u'name': u'module1', u'directive': u'install'}, {u'name': u'module2', u'directive': u'remove'}, {u'name': u'foobar', u'directive': u'tbd'}]
```
  
# yaml module
Yaml is functionally equivelant to json, but it is MUCH easier to write by hand.  It's a lot easier
to write valid yaml w/o making syntax mistakes... 

**yaml.load**
This will accept either a string with yaml content or a file handle (2nd example), and returns
python data. 
```python
In [54]: yaml_content
Out[54]: '\n- module: "python basics"\n  content:\n  - name: "prob1"\n    desc: "foo"\n  - name: "prob2"\n    desc: "foo2"\n- module: "python advanced"\n  content:\n  - name: "prob 1"\n    desc: "foo3"\n'

In [55]: print yaml_content

- module: "python basics"
  content:
  - name: "prob1"
    desc: "foo"
  - name: "prob2"
    desc: "foo2"
- module: "python advanced"
  content:
  - name: "prob 1"
    desc: "foo3"

In [56]: py_content = yaml.load(yaml_content)

In [57]: py_content
Out[57]: 
[{'content': [{'desc': 'foo', 'name': 'prob1'},
   {'desc': 'foo2', 'name': 'prob2'}],
  'module': 'python basics'},
 {'content': [{'desc': 'foo3', 'name': 'prob 1'}],
  'module': 'python advanced'}]
```
  
And from a file:  
```python
In [64]: with open('stuff.yaml', 'r') as f:
    ...:     py_data = yaml.load(f)
    ...:     

In [66]: py_data
Out[66]: 
[{'content': [{'desc': 'foo', 'name': 'prob1'},
   {'desc': 'foo2', 'name': 'prob2'}],
  'module': 'python basics'},
 {'content': [{'desc': 'foo3', 'name': 'prob 1'}],
  'module': 'python advanced'}]
```

**yaml.dump**  
This will dump to a file or return a string, dpeneding on the arguments passed to it.  
```python
In [69]: yaml_string = yaml.dump(py_data)

In [70]: print yaml_string
- content:
  - {desc: foo, name: prob1}
  - {desc: foo2, name: prob2}
  module: python basics
- content:
  - {desc: foo3, name: prob 1}
  module: python advanced

In [71]: with open('data.yaml', 'w') as f:
    ...:     yaml.dump(py_data, f)
    ...:     

In [72]: print open('data.yaml', 'r').read()
- content:
  - {desc: foo, name: prob1}
  - {desc: foo2, name: prob2}
  module: python basics
- content:
  - {desc: foo3, name: prob 1}
  module: python advanced

In [73]: 

```

# re module - regular expressions
The python re module uses unix/perl style regular expressions.  I often use this for validating
user input.  
  
There are lots of websites that are really useful for writing/testing regular exrepssions when
you're building one to use in a program.  Ex: https://regex101.com/  
  
**simple matching exmaple**
```python
In [88]: import re

In [89]: for f in os.listdir('.'):
    ...:     if re.match('[a-z]*.yaml', f):
    ...:         print f
    ...:         
    ...:     
data.yaml
stuff.yaml
```
  
Regular expressions can be compiled if they're going to be used a lot. This can iprove performance
for large data sets.  
```python
In [90]: exp = re.compile('[a-z]*.yaml')

In [91]: exp
Out[91]: re.compile(r'[a-z]*.yaml')

In [92]: for f in os.listdir('.'):
    ...:     if exp.match(f):
    ...:         print f
    ...:         
data.yaml
stuff.yaml
```
  
# sql and sqlite
sqlite is super useful if you need a local sql-like database and no hassles to get something
working.  It creates a DB on the local filesystem.  
https://docs.python.org/2/library/sqlite3.html  
  
This is one case where it's likely not appropriate to use the "with" convention (as I have it here).
You likely don't want to open and cose a cursor repeatedly if you're making lots of calls to the DB.
You can do `conn = sqlite3.connect('example.db')` and call `conn.close()` later if you're
going that route. 
```python
In [95]: with sqlite3.connect('example.db') as conn:
    ...:     c = conn.cursor()
    ...:     c.execute('''CREATE TABLE stocks
    ...:              (date text, trans text, symbol text, qty real, price real)
    ...: ''')
    ...:     c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100
    ...: ,35.14)")
    ...:     conn.commit()
    ...:     

In [98]: with sqlite3.connect('example.db') as conn:
    ...:     c = conn.cursor()
    ...:     c.execute('''select * from stocks''')
    ...:     print c.fetchall()
    ...:     
[(u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14)]
```
  
# xlsx

# pandas
