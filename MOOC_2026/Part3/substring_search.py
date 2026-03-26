input_string = "test"

print("t" in input_string)
print("x" in input_string)
print("es" in input_string)
print("ets" in input_string)


second_input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")

    if substring in second_input_string:
        print("Found it")
    else:
        print("Not Found")