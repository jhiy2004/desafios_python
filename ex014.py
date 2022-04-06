def fahrenheit(celsius):
    temp_fahrenheit = (celsius * 9/5) + 32
    return round(temp_fahrenheit, 1)


temp_celsius = float(input('Digite a sua temperatura em °C: '))
temp_fahrenheit = fahrenheit(temp_celsius)

print(f'A temperatura de {temp_celsius}°C corresponde a {temp_fahrenheit}°F')
