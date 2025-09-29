def unit_converter():
    print("\n===== Unit Converter =====")
    print("1. Kilometer → Miles")
    print("2. Miles → Kilometer")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km * 0.621371:.2f} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles / 0.621371:.2f} km")
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
    elif choice == "4":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")
    else:
        print("❌ Invalid choice")

unit_converter()