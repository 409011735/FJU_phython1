def power(x, n):
    return x ** n

x = int(input("請輸入整數x的值："))
n = int(input("請輸入次方數n的值："))

result = power(x, n)
print(f"{x} 的 {n} 次方為 {result}")