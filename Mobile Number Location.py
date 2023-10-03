import requests
import phonenumbers

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

mobileNo = input("Enter Mobile Number with Country Code: ")
parsed_number = phonenumbers.parse(mobileNo)

url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={parsed_number.latitude},{parsed_number.longitude}&key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Coordinates:", parsed_number.latitude, parsed_number.longitude)
else:
    print("Error:", response.text)
