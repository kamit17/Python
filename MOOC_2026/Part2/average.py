sum_values = 0 # a container to store the sum of integer values collected
num_count = 0  # a container to store the number of ineger valutes collected

input_string = input("Enter an integer. Enter nothing to quit: ")

while input_string:
    sum_values += int(input_string)
    num_count += 1
    input_string = input("Enter an integer. Enter nothing to quit: ")
    
avg = sum_values / num_count

print(f"Average is {avg}")