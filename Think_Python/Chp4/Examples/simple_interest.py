def final_amount(p,n,r,t):
    """
        Apply the compound interest formula to p to produce
        the final amount.
    """
    
    a = p * ( 1+ r/n) ** (n ** t)
    return a  # returning the value.

#calling the function
toInvest = float(input("how much do you want to invest?"))
fnl = final_amount(toInvest, 0.08,12,5)
print("At the end of the period you'll have", fnl)