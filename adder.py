def my_adder(a, b, c):
    out = a + b + c
    print(f"The value 'out' within the function is {out}")
    return out

out = 1
d = my_adder(1, 2, 3)
print(f"The value 'out' outside the function is {out}")
