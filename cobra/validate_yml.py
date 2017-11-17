from util import editor_utility as eu

def validate(yml):
    for label in eu.get_question_labels(yml):
        eu.print_question_data(yml, label)
    
if __name__ == '__main__':
    #files = ['enabled/2_basic_python.yml', 'enabled/3_files_paths.yml']
    #files = ['enabled/test.yml']
    files = ['enabled/3_problems.yml']
    #files = ['enabled/2_basic_python.yml']
    #files = ['enabled/test.yml']
    for file in files:
        validate(file)
