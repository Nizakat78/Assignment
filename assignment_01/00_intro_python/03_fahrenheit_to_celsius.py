# def convert_f_to_c(temp_in_fahrenheit):
#     return (temp_in_fahrenheit - 32) * 5 / 9

# tempf = float(input('Fahrenheit? '))
# tempc = convert_f_to_c(tempf)
# print(f'{tempc:.3f} degC')



convert_f_to_c =int(input("Enter the temperature in Fahrenheit:"))
temp_in_celsius = (convert_f_to_c -32) * 5/9
print(f"Temperature: {convert_f_to_c :.2f} = {temp_in_celsius :.10f}C")