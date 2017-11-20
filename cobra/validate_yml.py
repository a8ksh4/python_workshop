<<<<<<< HEAD
from util import editor_utility as eu

def validate(yml):
    for label in eu.get_question_labels(yml):
        eu.print_question_data(yml, label)
    
if __name__ == '__main__':
    #files = ['enabled/2_basic_python.yml', 'enabled/3_files_paths.yml']
    #files = ['enabled/test.yml']
    #files = ['enabled/2_problems.yml']
    #files = ['enabled/2_problems.yml']
    files = ['enabled/milestone2.yml']
    for file in files:
        validate(file)
=======
#!/usr/bin/env python

import sys
from util import editor_utility as eu

def validate(yml):
    for label in eu.get_question_labels(yml):
        eu.print_question_data(yml, label)
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        #files = ['enabled/2_basic_python.yml', 'enabled/3_files_paths.yml']
        #files = ['enabled/test.yml']
        files = ['enabled/2_problems.yml']
        #files = ['enabled/3_problems.yml']
        #files = ['enabled/test.yml']
    else:
        files = [sys.argv[1]]

    for file in files:
        validate(file)
>>>>>>> d080acc88c3803a5e6b70b41d5c82d44c3a1a669
