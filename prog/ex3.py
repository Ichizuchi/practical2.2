import math

if __name__ == "__main__":
    n = int(input("Чему равен n? "))
x = float(input("Чему равен x? "))
S = 0.0
for k in range(1, n + 1):
    a = math.log(k * x) / (k * k)
S += a
print(f"S = {S}")
