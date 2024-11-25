def main():

    # Take user input as a float
    print("This program can convert numerical amounts for a check into the properly formatted words.\n"
          "Please dont use commas in the input. Use a decimal as expected to designate cents\n"
          "Maximum conversion value is $99,999.99\n")
    check_amount = float(input("Type the check amount you want to convert : $"))
    # Int always rounds down so will always return dollar amount without cents
    check_amount_dollars = int(check_amount)
    # Cents = Total amount - Dollar amount x 100. Round is for better output
    check_amount_cents = round((check_amount - check_amount_dollars) * 100)
    # better format for cents with leading zeros
    zero_through_nine_cents = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if check_amount_cents < 10:
        check_amount_cents = zero_through_nine_cents[check_amount_cents]
    # list of numbers 1-99 is to account for hyphens in english language most easily.
    numbers_in_words = [
        '', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
        "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven",
        "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two",
        "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven",
        "thirty-eight", "thirty-nine", "forty", "forty-one", "forty-two", "forty-three",
        "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight",
        "forty-nine", "fifty", "fifty-one", "fifty-two", "fifty-three", "fifty-four",
        "fifty-five", "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine",
        "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five",
        "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine", "seventy",
        "seventy-one", "seventy-two", "seventy-three", "seventy-four", "seventy-five",
        "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine", "eighty",
        "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five",
        "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine", "ninety",
        "ninety-one", "ninety-two", "ninety-three", "ninety-four", "ninety-five",
        "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine"
    ]
    print("\nConverted value = ", end='')

    if check_amount_dollars == 0:
        print("Zero dollars and {}/100".format(check_amount_cents))

    elif 0 < check_amount_dollars < 100:
        print("{} dollars and {}/100".format(numbers_in_words[check_amount_dollars].capitalize(),
                                             check_amount_cents))
    elif 100 <= check_amount_dollars < 1000:
        hundreds_place = int(check_amount_dollars / 100)
        tens_place = check_amount_dollars % 100
        print("{} hundred {} dollars and {}/100".format(numbers_in_words[hundreds_place].capitalize(),
                                                        numbers_in_words[tens_place], check_amount_cents))
    elif 1000 <= check_amount_dollars < 100000:
        thousands_place = int(check_amount_dollars / 1000)
        hundreds_place = int(check_amount_dollars / 100) % 10
        tens_place = check_amount_dollars % 100
        if hundreds_place == 0:
            print("{} thousand {} dollars and {}/100".format(numbers_in_words[thousands_place].capitalize(),
                                                             numbers_in_words[tens_place], check_amount_cents))
        else:
            print("{} thousand {} hundred {} dollars and {}/100".format(numbers_in_words[thousands_place].capitalize(),
                                                                        numbers_in_words[hundreds_place],
                                                                        numbers_in_words[tens_place],
                                                                        check_amount_cents))

    else:
        print("Number is too big, try again with a number less than $100,000.00")


if __name__ == "__main__": main()