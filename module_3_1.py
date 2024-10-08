calls = 0
def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    global calls
    len_ = len(string)
    str_ = string.upper()
    str_1 = str_.lower()
    tuple_ = (len_, str_, str_1)
    return  tuple_

print(string_info('kookaburra'))
count_calls()
print(string_info('caterpillar'))
count_calls()
print(string_info('paragraph'))
count_calls()


list_to_search = ['word_', 'word_2', 'word_3']
string = 'word'
def is_contains(string, list_to_search):
     global calls
     if string in list_to_search:
        print(True)
     else:
        print(False)

is_contains('resent', ['resent', 'require', 'return'])
count_calls()
is_contains('custom', ['convert', 'control', 'current'])
count_calls()

print(calls)
