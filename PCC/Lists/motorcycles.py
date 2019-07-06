motorcycles = ['honda','ducati','suzuki']
motorcycles.append('BMW')
motorcycles.append('Aprilla')

print(motorcycles)
print('####################################')

motorcycles.insert(0, 'KTM')
print(motorcycles)
print('####################################')
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print('####################################')
print(popped_motorcycles)