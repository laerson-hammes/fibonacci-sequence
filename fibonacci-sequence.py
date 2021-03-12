a = 0
b = 1
fibonacci = []
for i in range(0, 50):
   fibonacci.append(a)
   a, b = b, a + b

print(fibonacci)