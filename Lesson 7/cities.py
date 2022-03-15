cities = {"Bratislava":
              {'population': 437120,
               'country': 'Slovakia',
               'fact': 'is a rich yet affordable city'},
          "Brussels":
              {'population': 2096000,
               'country': 'Belgium',
               'fact': 'has 138 restaurants per each 2.6 square km'},
          "Port Louis":
              {'population': 148147,
               'country': 'Mauritius',
               'fact': 'was renamed after Louis XV the French took control in 1736'}}
for key, value in cities.items():
    print(f"{key} is located in {cities[key]['country']}. {key} has a population of {cities[key]['population']}."
          f" Did you know that {key} {cities[key]['fact']}.")
    print('----------------------------------------------------')

