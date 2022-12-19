import math

print("Jeena Vinod Kumar, 32")
print("input x1=")
x1 = float(input())
print("input x2=")
x2 = float(input())
print("input Bias b=")
b = float(input())
print("input weight w1=")
w1 = float(input())
print("input weight w2=")
w2 = float(input())

yin = b + (x1 * w1) + (x2 * w2)

Y1 = 1 / (1 + math.exp(-yin))
Y2 = (1 - math.exp(-yin)) / (1 + math.exp(-yin))
print("Binary sigmoid activation function")
print("Y1=", Y1)
print("Y2=", Y2)
print("Done")