# File: Week 12 Program.py
# Name: Jeff Peterson
# Date: 05/31/2019
# Course: DSC510-T301
# Desc: This program provides general weather conditions from Openweathermap.org.
# Usage: The user enters either a zip code or city name.

import requests
from uszipcode import SearchEngine

print("Welcome to the Weather Program application.")
inputValue = input("Would you like to get the weather?  Enter either y or n.").casefold()

def main():
    city = input("Please enter location zip code or city name: ")
    print()
    try:
        query = "q=" + city  #this section searches zip code database to make sure the location entered exists
        weatherData = get_weather(query)  #zip code database must load the first time you run the program
        printReport(weatherData, city)
        print()
    except:
        print("City name not found.")


def printReport(weatherData, city):
    degree_sign = u'\N{DEGREE SIGN}' + "F"  #if using metric units, change F to C
    current_temp = weatherData["main"]["temp"]
    current_conditions = weatherData["weather"][0]["main"]
    current_ws = weatherData["wind"]["speed"]
    current_humidity = weatherData["main"]["humidity"]
    print("-------------------------------")
    print("Current weather in " + city + " is:")
    print(current_temp,degree_sign, current_conditions)
    print("Wind speed: " + str(current_ws) + " mph") #if using metric units, change mph to m/s
    print("Humidity: " + str(current_humidity) + "%")
    try:
        """If the user enters a zip code, this section will return the name of the city"""
        search = SearchEngine(simple_zipcode=True)
        zipcode = search.by_zipcode(city)
        print("The city name of the zip code you entered is: " + zipcode.major_city)
    except:
        print()
    print("-------------------------------")


def get_weather(query):
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?" + query + "&APPID=43e4544b641422894628e7dd582d8759&units=imperial")  #if you want different units, change "imperial" to "metric"
        if response.status_code == 200:
            print("Connection successful.")
            res = response.json()
            return res
    except requests.exceptions.RequestException as error:
        print(error)

cont = "y"
while cont == "y":
    if inputValue == "y":
        main()
    elif inputValue == "n":
        print("You selected no.  Program will end.")
        exit()
    else:
        print("You made an invalid entry.  Program will exit.")
        exit()
    cont = input("Would you like to continue?")
    if cont == "n":
        print("You selected no.  Program will end.")
        exit()

main()