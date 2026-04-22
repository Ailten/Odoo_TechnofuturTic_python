
# read a file txt with yield.

def readFile(path_file):
    with open(path_file, 'r') as file:
        for line in file:
            yield line.strip()

path_txt = 'Module04_Function\\text.txt'
list_line = readFile(path_txt)
print('\n'.join(list_line))

word_count = sum([1 for _ in list_line])
print(word_count)


from utils.file_utils import my_function, my_function_2  # import a function from a file (in a package).
#from utils.file_utils import *  # import all.