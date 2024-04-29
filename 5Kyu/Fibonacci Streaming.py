def all_fibonacci_numbers():
    for i in range(2):
        yield i
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b
def fibonacci(n):
    return list(all_fibonacci_numbers())[n]

print(fibonacci(30)) 