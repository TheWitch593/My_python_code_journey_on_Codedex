numeral_input = input("Enter the roman numerals you want to convert: ")
numeral_input1 = int(input("Enter the integer you want to convert: "))

def roman_to_int(numeral):
    final_answer = 0
    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1
    print(f"The roman numerals you entered translates to: {final_answer} !")

def int_to_roman(numeral):
    final_answer = ""
    while numeral != 0:
        if numeral >= 1000:
            final_answer += "M"
            numeral -= 1000
        elif numeral >= 900:
            final_answer += "CM"
            numeral -= 900
        elif numeral >= 500:
            final_answer += "D"
            numeral -= 500
        elif numeral >= 400:
            final_answer += "CD"
            numeral -= 400
        elif numeral >= 100:
            final_answer += "C"
            numeral -= 100
        elif numeral >= 90:
            final_answer += "XC"
            numeral -= 90
        elif numeral >= 50:
            final_answer += "L"
            numeral -= 50
        elif numeral >= 40:
            final_answer += "XL"
            numeral -= 40
        elif numeral >= 10:
            final_answer += "X"
            numeral -= 10
        elif numeral >= 9:
            final_answer += "IX"
            numeral -= 9
        elif numeral >= 5:
            final_answer += "V"
            numeral -= 5
        elif numeral >= 4:
            final_answer += "IV"
            numeral -= 4
        elif numeral >= 1:
            final_answer += "I"
            numeral -= 1
    print(f"The integer you entered translates to: {final_answer} !")

roman_to_int(numeral_input)
int_to_roman(numeral_input1)