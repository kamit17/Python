days_late = int(input("How many days late the book is: "))
is_overdue = (days_late >0 and days_late <=7)
has_fine = (days_late > 7 )
print("Thanks for returning the book.")
if is_overdue:
    print("This book is overdue")
if has_fine:
    print("You must pay a fine.")
    
