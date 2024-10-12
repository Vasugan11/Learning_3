calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    len_ = len(string)
    str_ = string.upper()
    str_1 = str_.lower()
    tuple_ = (len_, str_, str_1)
    count_calls()
    return  tuple_

print(string_info('kookaburra'))
print(string_info('caterpillar'))
print(string_info('paragraph'))


list_to_search = ['word_', 'word_2', 'word_3']
string = 'word'
def is_contains(string, list_to_search):
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    cont = True
    if string not in list_to_search:
        cont = False
    count_calls()
    return cont


print(is_contains('resent', ['Resent', 'require', 'return']))
print(is_contains('custom', ['convert', 'control', 'current']))
print(is_contains('ensure', ['entire', 'Ending', 'enable']))


print(calls)