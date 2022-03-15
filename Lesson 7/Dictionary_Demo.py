# alien_o = {'color': 'green', 'points': 5}
# print(alien_o)
# print(alien_o['color'])
# print(alien_o['points'])
# # print('====================================')
# alien_o['color'] = 'red'
# print(alien_o)
# print(alien_o['color'])
# print('====================================')
# alien_o['num_eyes'] = 5
# print(alien_o)
# print('====================================')
# alien_o['color'] = 'light' + alien_o['color']
# print(alien_o['color'])
# print('====================================')
# del alien_o['num_eyes']
# print(alien_o)
#
# for key, value in alien_o.items():
#     print(f'Key: {key}')
#     print(f'Value: {value}')
#
# print('====================================')
# for key in alien_o():
#     print(f'Key: {key}')
#     print(f'Value" {alien_o[key]}')
#
# print('====================================')
# # print(alien_o['health'])
# print(alien_o.get('health', 'Invalid key'))
#
print('====================================')
aliens = {
    'alien_0': {
        'color': 'green',
        'points': 5},
    'alien_1': {
        'color': 'yellow',
        'points': 10},
    'alien_2': {
        'color': 'red',
        'points': 15}}

for alien, alien_property in aliens.items():
    print(alien)
    for key in alien_property.keys():
        print(f'{key}: {alien_property[key]}')

    print('-----------')

print('====================================')

colors = ['white', 'black', 'blue', 'brown']
points = [6, 7, 8, 10]
index = 0
num = len(aliens)
while num < 7:
# for num in range(7):
    # aliens['alien_' + str(num)] = {'color': 'green', 'points': 5}
    aliens['alien_' + str(num)] = {'color': colors[index], 'points': points[index]}
    index = index + 1
    num = num + 1

for alien, alien_property in aliens.items():
    print(alien)
    for key in alien_property.keys():
        print(f'{key}: {alien_property[key]}')

    print('-----------')
