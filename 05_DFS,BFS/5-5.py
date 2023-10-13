#팩토리얼

def factorial(i):
    if i<=1:
        return 1
    return i* factorial(i-1)



r=factorial(5)
print(r)