a = 0
b = 1
fibonacci = []
for _ in range(50):
   fibonacci.append(a)
   a, b = b, a + b

print(fibonacci)