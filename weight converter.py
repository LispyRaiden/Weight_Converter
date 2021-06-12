kilograms_pos = ['kilogram', 'kilograms', 'kg', 'Kilogram', 'Kilograms']
pounds_pos = ['pounds', 'Pounds', 'pound', 'Pounds', 'lb', 'lbs']
grams_pos = ['gram', 'grams', 'Grams', 'Gram', 'g']
tons_pos = ['Tons', 'tons', 'Ton', 'ton', 't']

print("Insert -start- to Begin")
start_pos = ['start', 'Start']
x = input()
if x in start_pos:
    print('We can convert')
    print('Kilogram')
    print('Grams')
    print('Pounds')
    print('Tons')
    print('What is the unit you have?')
    user_unit = input()
    print("What do you want to convert to?")
    unit = input()
    print(f"What is the the value of {user_unit}")
    unit_value = int(input())
    if user_unit in kilograms_pos:
        def kilogram_to_pounds():
            return print(f"{unit_value * 2.205} Pounds")


        def kilogram_to_grams():
            return print(f"{unit_value * 1000} Grams")


        def kilogram_to_tons():
            return print(f"{unit_value / 907} Tons")


        if unit in pounds_pos:
            kilogram_to_pounds()
        elif unit in tons_pos:
            kilogram_to_tons()
        elif unit in grams_pos:
            kilogram_to_grams()
        else:
            print("Error: Restart")
        print("Thank You for using the Weight Converter!!")

    elif user_unit in pounds_pos:
        def pound_to_kilograms():
            return print(f"{unit_value / 2.205} Kilograms")


        def pound_to_grams():
            return print(f"{unit_value * 454} Grams")


        def pound_to_tons():
            return print(f"{unit_value / 2000} Tons")


        if unit in kilograms_pos:
            pound_to_kilograms()
        elif unit in grams_pos:
            pound_to_grams()
        elif unit in tons_pos:
            pound_to_tons()
        else:
            print("Error: Restart")
        print("Thank You for using the Weight Converter!!")

    elif user_unit in grams_pos:
        def gram_to_kilograms():
            return print(f"{unit_value / 1000} Kilograms")


        def gram_to_pounds():
            return print(f"{unit_value / 454} Pounds")


        def gram_to_tons():
            return print(f"{unit_value / 907185} Tons")

        if unit in kilograms_pos:
            gram_to_kilograms()
        elif unit in pounds_pos:
            gram_to_pounds()
        elif unit in tons_pos:
            gram_to_tons()
        else:
            print("Error: Restart")
        print("Thank You for using the Weight Converter!!")

    elif user_unit in tons_pos:
        def ton_to_kilograms():
            return print(f"{unit_value * 907} Kilograms")


        def ton_to_grams():
            return print(f"{unit_value * 907185} Grams")


        def ton_to_pounds():
            return print(f"{unit_value * 2000} Pounds")

        if unit in kilograms_pos:
            ton_to_kilograms()
        elif unit in grams_pos:
            ton_to_grams()
        elif unit in pounds_pos:
            ton_to_pounds()
        else:
            print("Error: Restart")
        print("Thank You for using the Weight Converter!!")
else:
    print("Error: Restart")