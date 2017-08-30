# The code in this quiz generates weather report alerts. The original programmer used string concatenation to assemble the alerts though, which resulted in some hard to read code. 
# Rewrite the code using the format method. Your new code should produce the same string as the old code you're replacing.

city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#todo rewrite this line to use the format method rather than string concatenation
alert = "Today's forecast for " + city + ": The temperature will range from " + str(low_temperature) + " to " + str(high_temperature) + " " + temperature_unit + ". Conditions will be " + weather_conditions + "."

alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city, low_temperature, high_temperature, temperature_unit, weather_conditions)
# print the alert
print(alert)


# The output is : Today's forecast for Seoul: The temperature will range from 9 to 18 degrees Celsius. Conditions will be light rain.