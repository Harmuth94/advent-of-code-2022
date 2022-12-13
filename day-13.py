
def make_list(x):
    if isinstance(x, list):
        return x
    else:
        return [x]

def compare_values(left_list, right_list):
    for i in range(len(left_list)):
        left_value = left_list[i]
        try:
            right_value = right_list[i]
        except IndexError:
            return False
        if isinstance(left_value, list) or isinstance(right_value, list):
            result = compare_values(make_list(left_value), make_list(right_value))
            if result is None:
                continue
            else:
                return result
        else:
    
            if left_value == right_value:
        
                continue
            if left_value < right_value:
        
                return True
            else:
        
                return False
    if len(left_list) < len(right_list):
        return True
# read input
with open("input-13.txt", "r") as f:
    sample_input = f.read()

# parse input
sample_input = sample_input.split('\n\n')
sample_input = [x.split('\n') for x in sample_input]
sample_input = [[eval(y) for y in x] for x in sample_input]
ind_sum = 0
for i, sample in enumerate(sample_input):
    check = compare_values(sample[0], sample[1])
    if check:
        ind_sum += (i + 1)

print(ind_sum)

one_list_sample = [y for x in sample_input for y in x]
one_list_sample.append([[2]])
one_list_sample.append([[6]])

def get_key(x):
    return sum([compare_values(y, x) or False for y in one_list_sample])
    
# brute forced it
sorted_list = sorted(one_list_sample, key=get_key)

print((sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1))