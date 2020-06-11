from test_suite import test

def count(sub_string,string):
    """Count the number of times a sub string appears in a string"""
    appearences = 0
    last_found_at = -1
    while True:
        last_found_at = string.find(sub_string, last_found_at + 1)
        if last_found_at == -1:
            return appearences
        else:
            appearences += 1

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)
