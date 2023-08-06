translations = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

while True:
    try:
        number = 0
        roman_number = input("Enter roman number: ")

        if "IIII" in roman_number:
            print("Error, Try again")
        else:
            roman_number = roman_number.replace("IV", "IIII").replace("IX", "VIIII")
            roman_number = roman_number.replace("XL", "XXXX").replace("XC", "LXXXX")
            roman_number = roman_number.replace("CD", "CCCC").replace("CM", "DXXXX")

            for char in roman_number:
                if char not in translations.keys():
                    print("Error, Try again")
                else:
                    number += translations[char]
            if number < 5000:
                print(number)
            else:
                print("Enter more less number!")

    except KeyboardInterrupt:
        print("Finished")
        break


