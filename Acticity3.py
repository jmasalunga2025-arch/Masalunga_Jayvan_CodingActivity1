def collatz(n):
    if n % 2 == 0:
        Even_result = n // 2
        print(Even_result)
        return Even_result
    else:
        Odd_result = 3 * n + 1
        print(Odd_result)
        return Odd_result
    
try:
    user_num = int(input("Enter a starting number: "))

    if user_num <= 0:
        print("Plese enter only a positive number and higher than 0!")
    else:
        while user_num != 1:
            user_num = collatz(user_num)

except ValueError:
    print("Invalid input! Plese enter a whole number.")
