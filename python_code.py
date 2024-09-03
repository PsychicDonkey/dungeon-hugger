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

#add elements to list
exact_microsoft_companies = []
for company_info in microsoft_companies:
    if company_info['fields']['name'] == "microsoft":
        exact_microsoft_companies.append(company_info)
print(len(exact_microsoft_companies))

#create a table from a JSON
all_products = []
for category in gwz_products_translated:
    for subcategory in gwz_products_translated[category]:
        for product in gwz_products_translated[category][subcategory]:
            all_products.append({'category' : category ,'subcategory' : subcategory,'product' : product})
df=pd.DataFrame(all_products)
df #will show the dataframe
