a=int(input())
for i in range(a):
    b=input().split()
    try:
        print(int((int(b[0])/int(b[1]))))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except Exception as w:
        print("Error Code:",w)
#exception print
