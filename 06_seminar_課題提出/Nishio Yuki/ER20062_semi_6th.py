import numpy as np
import matplotlib.pyplot as plt
# 課題1
a = ["m","c","i","e","p","r","e","t","o"," ","o","o","i","s","g","o","p"]
b = ["a","h","n"," ","e","c","p","i","n","r","b","t","c","-","r","u","!"]
text = []

for n,m in zip(a,b):
    text.append(n+m)

for ch in text:
    print(ch,end =  "")



#課題2
ans = []
count = 0
sum = 0
var = 0
math = np.array([40,15,72,22,43,82,75,7,34,49,95,75,85,47,63])
for i in math:
    sum += i
    if i >= 70:
        count += 1
print("70点以上:" + str(count)) #70点以上の人数を計算

def standard(n,axis = None, ddof = 0): #標準化のための関数
    mean = n.mean()
    std = n.std()
    standard = (n - mean) / std
    return standard

print(standard(math)) # 標準化後の配列



#課題3
x = np.arange(-5.0,5.0,0.1)
def sigmoid(x):
    return 1/(1 + np.exp(-x))
def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x
def tanh(x):
    return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-
    x))

plt.title("functions")
plt.xlabel("input")
plt.ylabel("output")
plt.plot(x,sigmoid(x),label = "sigmoid")
plt.plot(x,softmax(x),label = "softmax")
plt.plot(x,tanh(x),label = "tanh")
plt.grid()
plt.legend()

plt.show()
