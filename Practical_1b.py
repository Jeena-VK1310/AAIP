print("Jeena Vinod Kumar, 32")

print("input x1= ")
x1 = float(input())
print("Input x2= ")
x2 = float(input())
print("Input x3= ")
x3 = float(input())

print("Input Weight w1= ")
w1 = float(input())
print("Input Weight w2= ")
w2 = float(input())
print("Input Weight w3= ")
w3 = float(input())

print("Input Bias b= ")
b = float(input())

yin = b + (x1 * w1 + x2 * w2 + x3 * w3)

if yin >= 0:
    y = 1
else:
    y = 0
print("Inputs are:")

print("x1=", x1)
print("x2=", x2)
print("x3=", x3)

print("Weights are:")
print("w1=", w1)
print("w2=", w2)
print("w3=", w3)
print("Bias b= ", b)
print("Net Input yin = ", yin)
print("Output= ", y)
print("Done")
