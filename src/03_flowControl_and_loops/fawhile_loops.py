# WHILE LOOPS

# Initialize temperature variable
temperature = 70

# Loop until temperature reaches 80
while temperature < 80:
    print(f'The current temperature is {temperature}°F')  # Display current temperature
    temperature += 1  # Increase temperature by 1


# else statement with while.

configval = 50;
while configval > 45:
    print(f'value is too high: {configval=}')
    configval -= 2;
else: #This else is associated with while looop. it gets executed when while loop successfully completed
    print(f'config value is in acceptable range: {configval=}')