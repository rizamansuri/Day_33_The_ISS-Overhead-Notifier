# BismillahirRahminirRahim
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# It will raise and show exceptions if there are
response.raise_for_status()

# To get the data using api from website
data = response.json()
print(data)

# To get specific data from the dictionary
data = response.json()["iss_position"]
print(data)

# To get latitude only
data = response.json()["iss_position"]["longitude"]
print(data)

# Create tuple of latitude and longitude
latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
iss_position = (latitude,longitude)
print(iss_position)
