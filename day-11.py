import re

def parse_input(input_string: str) -> dict:
    # Split the input string into a list of strings, one for each monkey
    monkeys = input_data.split("\n\n")
    
    # Create an empty dictionary to store the parsed data
    parsed_data = {}
    
    # Loop through the list of strings, one for each monkey
    for monkey in monkeys:
        # Split the monkey string into lines
        lines = monkey.split("\n")
        
        # The first line contains the monkey number and starting items, so we
        # split that line on the colon to get the monkey number and starting items
        monkey_info = lines[0].split(":")
        
        monkey_number = int(monkey_info[0].split(" ")[1])
        starting_items = list(map(int, lines[1].split(':')[-1].split(", ")))
        
        # The second line contains the operation, so we split that line on the
        # colon to get the operation
        operation = eval('lambda old: '+lines[2].split(":")[1].split("=")[1])
        
        # The third line contains the test, so we split that line on the colon
        # to get the test

        test = int(re.findall(r'\d+', lines[3])[-1])
        
        # fetch int in end of string
        if_true = int(re.findall(r'\d+', lines[4])[-1])
        if_false = int(re.findall(r'\d+', lines[5])[-1])
        
        
        # Store the parsed data for the current monkey in the dictionary
        parsed_data[monkey_number] = {
            "starting_items": starting_items,
            "operation": operation,
            "test": test,
            "if_true": if_true,
            "if_false": if_false
        }
    
    # Return the parsed data
    return parsed_data

# read all input data
with open("input-11.txt") as f:
    input_data = f.read()

# parse the input data
parsed_data = parse_input(input_data)



n_monkeys = len(parsed_data)
inspected_items = {monkey_number: 0 for monkey_number in range(n_monkeys)}
for i in range(20):
    for monkey_number in range(n_monkeys):
        
        monkey_data = parsed_data[monkey_number]
        #print(f"Monkey {monkey_number}")
        
        while True:
            try:
                to_throw = monkey_data["starting_items"].pop(0)
            except IndexError:
                break
            #print("  Monkey inspected item {}".format(to_throw))
            inspected_items[monkey_number] += 1
            worry_level = int(monkey_data["operation"](to_throw)/3)
            #print("  Monkey is worried about item {}".format(worry_level))
            if worry_level % monkey_data["test"] == 0:
                #print(f"  Monkey is throwing item {worry_level} to {monkey_data['if_true']}")
                parsed_data[monkey_data["if_true"]]["starting_items"].append(worry_level)
            else:
                #print(f"  Monkey is throwing item {worry_level} to {monkey_data['if_false']}")
                parsed_data[monkey_data["if_false"]]["starting_items"].append(worry_level)


# parse the input data
parsed_data = parse_input(input_data)


from time import time
n_monkeys = len(parsed_data)
inspected_items = {monkey_number: 0 for monkey_number in range(n_monkeys)}

lcm = 1
for x in range(n_monkeys):
    lcm = lcm * parsed_data[x]["test"]

for i in range(10000):
    print(i)
    for monkey_number in range(n_monkeys):
        
        monkey_data = parsed_data[monkey_number]
        #print(f"Monkey {monkey_number}")
        
        while True:
            try:
                to_throw = monkey_data["starting_items"].pop(0)
            except IndexError:
                break
            #print("  Monkey inspected item {}".format(to_throw))
            inspected_items[monkey_number] += 1
            worry_level = monkey_data["operation"](to_throw)
            #print("  Monkey is worried about item {}".format(worry_level))
            start = time()
            worry_level %= lcm
            if worry_level % monkey_data["test"] == 0:
                #print(f"  Monkey is throwing item {worry_level} to {monkey_data['if_true']}")
                parsed_data[monkey_data["if_true"]]["starting_items"].append(worry_level)
            else:
                #print(f"  Monkey is throwing item {worry_level} to {monkey_data['if_false']}")
                parsed_data[monkey_data["if_false"]]["starting_items"].append(worry_level)
        
            end = time()