points = int(input("How many points are on your card?"))
#bonus_point= 
is_small_bonus = points < 100

if is_small_bonus:
    bonus_percent = 10
else:
    bonus_percent = 15

print(f"Your bonus is {bonus_percent}%")   

bonus_points = points * bonus_percent /100
new_total = points + bonus_points

print(f"You now have {new_total} points") 