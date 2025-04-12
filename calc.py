def basic_calculator():
    print("Basic Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operation!")
        return

    print(f"Result: {result}")

def scientific_calculator():
    print("Scientific Calculator")
    print("Available operations: sin, cos, tan, sqrt, log, exp")
    operation = input("Choose operation: ")
    num = float(input("Enter the number: "))

    import math
    if operation == 'sin':
        result = math.sin(math.radians(num))
    elif operation == 'cos':
        result = math.cos(math.radians(num))
    elif operation == 'tan':
        result = math.tan(math.radians(num))
    elif operation == 'sqrt':
        result = math.sqrt(num)
    elif operation == 'log':
        result = math.log(num)
    elif operation == 'exp':
        result = math.exp(num)
    else:
        print("Invalid operation!")
        return

    print(f"Result: {result}")

def bmi_calculator():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")

def temperature_converter():
    print("Temperature Converter")
    print("Available conversions: C to F, F to C")
    conversion = input("Choose conversion (CtoF or FtoC): ")
    temp = float(input("Enter the temperature: "))

    if conversion == 'CtoF':
        result = (temp * 9/5) + 32
        print(f"{temp}°C is {result}°F")
    elif conversion == 'FtoC':
        result = (temp - 32) * 5/9
        print(f"{temp}°F is {result}°C")
    else:
        print("Invalid conversion!")

def main():
    while True:
        print("\nMulti-Calculator Application - By Samin Yeasar")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. BMI Calculator")
        print("4. Temperature Converter")
        print("5. Exit")
        choice = input("Choose a calculator (1-5): ")

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            scientific_calculator()
        elif choice == '3':
            bmi_calculator()
        elif choice == '4':
            temperature_converter()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()