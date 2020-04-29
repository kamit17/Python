def is_divisble(x,y):
    """Test if x is exactly divisble by y"""
    if x % y == 0:
        return True
    else:
        return False
    
print(is_divisble(6,4))