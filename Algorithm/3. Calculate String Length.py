input_str = 'LucidProgramming'

print(len(input_str))

def iterative_str_len(input_str):
    count = 0
    for i in range (len(input_str)):
        count +=1
    return count

iterative_str_len(input_str)

def recursive_str_len(input_str):
    if input_str=='':
        return 0
    return 1+recursive_str_len(input_str[1:])

recursive_str_len(input_str)