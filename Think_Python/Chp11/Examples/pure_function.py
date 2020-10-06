def double_stuff(a_list):
    """ Returns a new list which contains doubles of the elements
    in a list."""

    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list

things = [2,5,9]
xs = double_stuff(things)
print(things)
print(xs)