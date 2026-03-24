# Count Fizz, Buzz, FizzBuzz

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, 51):

    if i % 3 == 0:
        print(i, "Fizz")
        fizz_count += 1

    if i % 5 == 0:
        print(i, "Buzz")
        buzz_count += 1

    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
        fizzbuzz_count += 1

# Output counts
print("\nCount Summary:")
print("Fizz:", fizz_count)
print("Buzz:", buzz_count)
print("FizzBuzz:", fizzbuzz_count)