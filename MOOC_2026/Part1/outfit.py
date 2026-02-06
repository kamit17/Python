temp = int(input("Temperature: "))
rain_input = input("will it rain ( yes/no):")
is_raining = (rain_input==  "yes")
print("Wear jeans and a T-shirt")
if temp <=20:
    print("I recommend a jumper as well")
if temp <=10:
    print("Take a jacket with you")
if temp <=5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if is_raining:
    print("dont forget your umbrella")