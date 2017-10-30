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
* listDirFilter(dir_path, filter)
  * 34
  * return a list of files at a given path whos names match the given filter. 
* createTmpDir(dir_name)
  * 33
  * create a directory in /tmp with the given name and return the path to the new directory
* realPath(path)
  * 34
  * given a path, find out if it contains a symlink.  If so, return the actual path to where the given path points. If no symlinks, return the given path. 
* filePaths(dir_path, files_list)
  * 34
  * given a directory path and a list of file, create a list of complete paths to each file (dir_path + file path)

## permissions
* tarDir(src_dir, dst_tar)
  * 34
  * given a source directory containing files, create a tar file at the given dst_tar (e.g. /tmp/my_stuff.tar) and add the
  directory and its contents into the tar file. 
# Tar
