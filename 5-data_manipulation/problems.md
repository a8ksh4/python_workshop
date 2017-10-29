# csv
* csvFileToArray(file_path) -> array
  * 50
  * read csv text data in from the given file and return it as an array (list of lists), aka list of rows. 
* arrayToCsvFile(file_path, array)
  * 50
  * convert array (list of lists) to csv and write to file. 
* dictToCsvFile(file_path, dict)
  * 51
  * use dict keys as column one, values (list) as other columns, sort by key and write to file. 
  
# json
* jsonFiletoData(file_path) -> data
  * 50
  * use json module to read json content from the given file, convert it to python data, and return the data.
* dataToJsonFile(file_path, data)
  * 50
  * use json module to convert a given data structure to json format and write it to file. 
  
# yaml
* yamlFiletoData(file_path) -> data
  * 50
  * use yaml module to read json content from the given file, convert it to python data, and return the data.
* dataToYamlFile(file_path, data)
  * 50
  * use yaml module to convert a given data structure to json format and write it to file. 

# regex
* simpleReTest(value, regex_string) -> bool
  * 50
  * given a value and a regex string, return True of the value matches the regex string or False if it
    does not. 
* filteredList(list, regex_string) -> list
  * 51
  * Given a list of strings, use the "re" modudule to regex match the regex_string against values
    in the list and return a list of matching strings.  Preserve order of the orignial list. 

# sql and sqlite
* createSqliteTable(db_file, table_name, table_columns, rows)
  * 54
  * given a filename, open a sqlite db using that file and create a new table using the given name and
    columns.  Then insert each of the provided rows of data and commit the change. If "rows" is an empty
    list, then do not insert any rows to the table you just created.  
* sqlitReadRows(db_file, table_name) -> array
  * 51
  * given a sqlite db file, query all of the rows in the given table, and return them as an array.
* sqlitReadRowsDict(db_file, table_name) -> list of dicts
  * 52
  * given a sqlite db file, query all of the rows in the given table, and a list of dictionaries, with
    each row being a dictionary with keys equal to the column names and values each value for that row. 
