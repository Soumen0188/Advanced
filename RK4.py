# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:48:00 2024

@author: Admin
"""

def f(x, y):
    return x + y

def rk4(x0, y0, xn, n):
    h = (xn - x0) / n
    print("\n--------SOLUTION--------")
    print("-------------------------")
    print("x0\ty0\ty_n")
    print("-------------------------")
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y_n = y0 + k
        print(f"{x0:.4f}\t{y0:.4f}\t{y_n:.4f}")
        y0 = y_n
        x0 += h
    print(f"\nAt x = {xn:.4f}, y = {y_n:.4f}")

# Inputs
x0 = float(input("Enter initial x (x0): "))
y0 = float(input("Enter initial y (y0): "))
xn = float(input("Enter calculation point (xn): "))
n_steps = int(input("Enter number of steps: "))

# Solve using RK4
rk4(x0, y0, xn, n_steps)
