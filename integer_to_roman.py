# Given an integer, convert it to a roman numeral. Input is guaranteed to be within
# the range from 1 to 3999



# Roman numerals are represented by seven symbols
# I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 10000
# "I" can be placed before "V" and "X" to make 4 and 9
# "X" can be placed before "L" and "C" 40 90
# "C" can be placed before "D" and "M" to make 400 and 900


#Input: 3 Output: III
#Input: 4 Output: IV
#Input: 9 Output: IX
#Input: 58 Output: LVIII

#start with input value 58 and divide by largest base which is 50
# Translate base dividend with correct symbol
# Keep dividing until remainder is None
# Return string

#Time complexity: 0(n^2) because we must loop through the numerical value and then translate to symbolic value

def convert_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900 , 1000]
    sym = ["I","IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = 12
    while number: 
        div = number // num[i]
        number %= num[i]
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
    

def main():
    number = input("Enter a number: ")
    number = int(number)
    print(convert_roman(number))


if __name__ == "__main__":
    main()


