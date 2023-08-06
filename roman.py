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
    roman_number = input("Enter roman number: ")
    if roman_number not in translations.keys():
        print("Error, Try again!")
        roman_number = input("Enter roman number: ")
    number = 0
    roman_number = roman_number.replace("IV", "IIII").replace("IX", "VIIII")
    roman_number = roman_number.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_number = roman_number.replace("CD", "CCCC").replace("CM", "DXXXX")

    for char in roman_number:
        number += translations[char]
    print(number)
