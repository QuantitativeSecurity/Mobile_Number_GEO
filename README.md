Mobile Number Geolocation Finder

This program is designed to find the geolocation of a mobile number by using the phonenumbers library to parse the mobile number and the Google Maps Geocoding API to get the location details.
Dependencies

    Python 3.x
    requests and phonenumbers libraries

You can install these libraries using pip:

bash

pip install requests phonenumbers

Usage

    Copy the code from the program and save it into a file named geolocation_finder.py.
    Replace "YOUR_API_KEY" with your actual Google Maps API key.
    Execute the program by running the following command in your terminal:

bash

python geolocation_finder.py

    When prompted, enter the mobile number along with the country code.

Program Overview

The program performs the following steps:

    Importing Necessary Libraries:
    The requests and phonenumbers libraries are imported for HTTP requests and phone number parsing, respectively.

    Setting Up API Key:
    Replace "YOUR_API_KEY" with your actual Google Maps API key.

    Getting User Input:
    The user is prompted to enter a mobile number along with the country code.

    Parsing Phone Number:
    The phonenumbers library is used to parse the input mobile number.

    Building URL:
    A URL is constructed using the parsed phone number information and the Google Maps Geocoding API.

    Sending HTTP Request:
    An HTTP GET request is sent to the Google Maps Geocoding API to get the geolocation details of the mobile number.

    Handling Response:
    The program checks the status code of the HTTP response. If it's 200 (OK), it extracts the geolocation information from the response and prints it. Otherwise, it prints an error message.

Output

The program outputs the geolocation coordinates of the entered mobile number, or an error message if the request to the Google Maps Geocoding API fails.
