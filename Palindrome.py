def is_palindrome():
    num = int(input("Enter a number"))
    temp = num
    rev = 0
    while num:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
        if rev == temp:
            print("The number is palindrome")
        else:
            print("The number is not palindrome")


is_palindrome()
