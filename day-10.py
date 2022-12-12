# read input file
with open("input-10.txt") as f:
    program = f.read().splitlines()


# The signal strength at each of the specified cycles
signal_strengths = []

# The current cycle and the current value of the X register
cycle = 0
x = 1

# The value to add to the X register (initialize to 0)
add_value = []

# Execute the program
crt = ""
for instruction in program:
    # Increment the cycle
    cycle += 1
    # If the current cycle is one of the specified cycles,
    # calculate and store the signal strength
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(cycle * x)
    
    print(x, cycle % 40 or 40)
    if x - (cycle % 40 or 40) >=-2 and x-(cycle % 40 or 40) <= 0:
        crt+="#"
        
    else:
        crt+="."
    # Update the value to add to the X register according to the instruction
    if instruction == "noop":
        # Do nothing
        pass
    elif instruction.startswith("addx"):
        # Extract the value to add to X from the instruction


        cycle += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * x)
        print(x, cycle % 40 or 40)
        if x - (cycle % 40 or 40) >=-2 and x-(cycle % 40 or 40) <= 0:
            crt+="#"
        else:
            crt+="."
        add_value = int(instruction.split(" ")[1])
        x += add_value
        
        

    
# Calculate and print the sum of the signal strengths
print(sum(signal_strengths))

import re
print(re.sub("(.{40})", "\\1\n", crt, 0, re.DOTALL))