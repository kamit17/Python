from test import test
def count_a(text):
    """Counts the number of times the letter a appears in a string."""
    count = 0
    for c in text:
        if c == "a":
            count += 1
        return count

test(count_a("banana")==3)
