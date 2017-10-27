Tier, description...

# Opening, reading, writing
* readFileToString(path_to_file) -> string
  * 30
  * Given a path to a file, read it's contents and return the contents as a string.
 
* readLinesfromFiles(path_to_file) -> list of strings
  * 30
  * Given a path to a file, read it's contents and return each line as a string in a list of all lines.

* appendLinetoFile(path_to_file, content)
  * 30
  * Given a path to a file and a string value, "content", write the content to a new line at the end of the file.
  
* truncateWriteFile(path_to_file, content)
  * 30
  * Given a path to a file and a string value, "content", write the content to the file, replacing anything that is
    already there.  If the fle doesnt' exist, it is assumend that it would be created. 
    
* rewriteInLower(source_file, dest_file):
  * 31
  * given a source file path and a destination file path, read the file from the source and then write it out to the 
    dest path in all lower-case. 
    
* removeWhitespace(file_path):
  * 32
  * given a file path, read in the file content.  remove whitespace from the start and end of each line. remove any empty
    or whitespace-only lines.  Then write the content back to the file replacing the original content.

# os module
## os basics
* moveAFile(source_path, dest_path)
  * 30
  * Given a source path and destination path, move the file from source to destination.
* cdAndWrite(dir_path, file_name, content)
  * 34
  * Change directory to the given "dir_path", then write the given content to the given file_name. 

