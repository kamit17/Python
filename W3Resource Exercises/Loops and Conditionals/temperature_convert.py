"""
Write a Python program to convert temperatures to and from celsius, fahrenheit. 
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
def convert(temp,unit):
    unit = unit.lower()

    if unit == 'c':
        temp = 9.0/5.0 * temp +32
       #
        return '%s degrees Farenheit'% temp
    if unit == 'f':
        temp =(temp-32) /9.0 * 5.0
        return '%s degress Celcius'% temp


intemp = int(input('What is the temperature?\n'))
inunit = str(input('What is the measure of unit (f or c ):\n'))

#print(convert(intemp,inunit))
print('The converted temperature is :',convert(intemp,inunit))


