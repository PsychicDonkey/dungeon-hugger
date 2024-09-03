#function to search in a dictionary
def get_key_value_from_city(city, key):
  output = f'{key} not defined'
  if key in city.keys():
    output =  city[key]
  return output

#function to search a dictionary embedded in a list
def retrieve_city_key_value_database(city_name, key):
    output = f"{city_name} doesn't exist or is not covered."
    for city in cities:
        if city['name'] == city_name:
            output=get_key_value_from_city(city,key)
    return output
