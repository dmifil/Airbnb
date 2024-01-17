import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv("C:/Users/Dmitrii Filimoshin/Desktop/Python/Assignment/Final Project/airbnb_listings.csv")

# Drop rows with missing values in the 'host_location' column
data.dropna(subset=['host_location'], inplace=True)

# Reset index after dropping rows
data.reset_index(drop=True, inplace=True)

data[['city', 'country']] = data['host_location'].str.split(', ', expand=True)
data['city'] = data['city'].str.strip()
data['country'] = data['country'].str.strip()


print("Hello this is the AirBnB.DOS")
#need to rename for easy typing, First we need to split data set for the countryes, and cityes for easy serach
#also need to rename first row for easy access

unique_cities = data['country'].unique()
print(f"You can chose next country: {unique_cities}")


selected_country = input("I would like to go:").capitalize()

# Filter rows where the country is 'Your_Country'
filtered_country = data[data['country'] == selected_country]

# Check if there are any rows for the selected country
if not filtered_country.empty:
    # Get the unique cities and their counts
    cities_for_selected_country = filtered_country['city'].unique()

    # Print the cities for the selected country
    print(f"Cities in {selected_country}:\n{cities_for_selected_country}")
else:
    print("Country not in the list. Check types or choose another country.")

selected_city = input("I would like to go to:").capitalize()

# idea for the city if it only one variant for the city just give this variant and 
#told to the user that it is only one variant for this city. if it is more than one 
#start filtering with price per night ofter it add filter for date availability
# Filter rows where the country is 'Your_Country'
filtered_city = data[data['city'] == selected_city]

if len(filtered_city) == 1:
    
    # Get the unique cities and their counts
    
    varians_for_selected_city = filtered_city[['country','city','listing_url','property_type','room_type','minimum_nights','price']]

    # Print the cities for the selected country
    print(f"\nWe have only this variant in {selected_city}:\n\n{varians_for_selected_city.to_string()}\n")
    
    additional_info = input("\nYou can get additional information about host and property from the list:\n"
                             "Description of the property - description\n"
                             "Overview of the neighborhood - neighborhood_overview\n"
                             "Host profile - host_url\n"
                             "Brief info about host - host_about\n"
                             "Property amenities - amenities\n"
                             "Host rating - review_scores_rating\n\n"
                             "Type here:").lower()
    
    additional_info = str(additional_info)
    print(filtered_city[additional_info].iloc[0])

else:
    
    max_price = float(input("Enter the maximum price you are willing to pay per night: "))
    filtered_city['price'] = pd.to_numeric(filtered_city['price'], errors='coerce')
   

    
    filtered_city_by_price = filtered_city.loc[filtered_city['price'] <= max_price]
    print(filtered_city_by_price)






