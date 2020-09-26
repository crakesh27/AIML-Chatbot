import os
import aiml
from weather import Weather

k = aiml.Kernel()

print("Parsing aiml files")
k.bootstrap(learnFiles="startup.aiml", commands="load aiml b")

while True:
    
    input_text = input("> ")
    
    if input_text == "quit":
        exit()

    response = k.respond(input_text)

    if response == "weather":
        try:    
            weather = Weather()

            loc = input("Please mention the place \n> ")
            day = input("Which day do you want? \n> ")
            location = weather.lookup_by_location(loc)  
            forecasts = location.forecast()
            time = k.respond(day)

            if time == "none":
                print ("didn't understand you :(")
                continue

            if location is not None and time == "5":
                for forecast in forecasts:
                    print("Date : " + forecast.date())
                    print("Weather Condition is: " + forecast.text())
                    print("Highest temp: " + forecast.high() + " F")
                    print("Lowest temp: " + forecast.low() + " F")   
            elif location is not None:
                forecast = forecasts[int(time)]
                print("Date : " + forecast.date())
                print("Weather Condition is: " + forecast.text())
                print("Highest temp: " + forecast.high() + " F")
                print("Lowest temp: " + forecast.low() + " F") 
                
        except AttributeError:
            print("Sorry didn't understand")
    else:
        try: 
            print (response)
        except AttributeError:
            print("Sorry didn't understand")