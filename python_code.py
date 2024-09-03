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

#function to replace
def modify_city_key_value(city_name, key, value):
    output = f"{city_name} doesn't exist or is not covered."
    for city in cities:
        if city['name'] == city_name:
            if key in city.keys():
                city[key]= value
                output = f"{key} has been updated for {city_name}."
            else:
                output = f"{key} doesn't exist."
    return output
