import utils

data = [
  {
    'Country': 'Colombia',
    'population': 500
  },
  {
    'Country': 'Bolivia',
    'population': 300
  }
]

def run():
  keys, values = utils.get_polulation()
  print(keys, values)
  
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)
  print(result)

if __name__ == '__main__':
run()