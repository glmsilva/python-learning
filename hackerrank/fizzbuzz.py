def fizzBuzz(n):
    # Write your code here
    if n > 0 and n < 2 * (10 ** 5):
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print(i)
    else:
        return None
fizzBuzz(15)
