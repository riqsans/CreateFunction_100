def convert_temperature(value, unit):
    if unit.upper() == 'C':
        result = (value * 9/5) + 32
        return str(value) + "°C is equal to " + str(result) + "°F"
    elif unit.upper() == 'F':
        result = (value - 32) * 5/9
        return str(value) + "°F is equal to " + str(result) + "°C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit"
    
print(convert_temperature(32, 'C'))  
print(convert_temperature(89.6, 'F'))  