def myreplace(old,new,s):
    """ Replace all occurrences of old with new in s. """
    ...
    return new.join(s.split(old))

print(myreplace(",", ";", "this, that, and some other thing")=="this;that;and some other thing")

