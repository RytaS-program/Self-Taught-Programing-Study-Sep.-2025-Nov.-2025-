try:
    a=input("type a number")
    b=input("type another")
    a=float(a)
    b=float(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Please input correctly")

def str_to_float(s):
    try:
        return float(s)
    except ValueError:
        print("数値に変換できませんでした")
        return None

a=input("type a number: ")
b=input("type another: ")

a=str_to_float(a)
b=str_to_float(b)

try:
    result=a/b
    print("結果：", result)
except(TypeError, ZeroDivisionError):
    print("Please input correctly")
