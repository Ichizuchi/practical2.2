import math
import sys

if __name__ == "__main__":
    a = float(input("Чему равен a? "))
    if a < 0:
        print("Ошибка!", file=sys.stderr)
        exit(1)

    x, eps = 1, 1e-10
    while True:
        xp = x
        x = (x + a / x) / 2
        if math.fabs(x - xp) < eps:
            break
