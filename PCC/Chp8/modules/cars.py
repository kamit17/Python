#import cars_function
#from cars_function import make_car
from cars_function import make_car as mc
#car = cars_function.make_car('subaru', 'outback', color='blue', tow_package=True)
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
car = mc('subaru', 'outback', color='blue', tow_package=True)
print(car)
