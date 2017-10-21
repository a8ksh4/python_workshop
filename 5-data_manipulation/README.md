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
**yaml.dump**

**yaml.load**

# re module

# sql and sqlite

# xlsx

# pandas
