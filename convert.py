import re

def x(arr):
    for a in range(len(arr)):
        if a+1 > len(arr):
            break
        if a+1 < len(arr) and re.compile(r"(\w+) (\w+)").match(arr[a] + " " + arr[a+1]):
            a1 = ''.join(r'[A-Za-z]' for x in arr[a])
            a2 = ''.join(r'[A-Za-z]' for x in arr[a+1])
            if re.match(a1, arr[a]) and re.match(a2, arr[a+1]):
                print(arr[a] + " " + arr[a+1])
                arr[a] = "{} {}".format(arr[a], arr[a+1])
                arr[a+1] = ""
            else: print("Not a match {} {}".format(arr[a], arr[a+1]))
    return arr


with open("data.txt", "r", encoding="utf-8") as file:
    f = file.read()
    arr = f.split(" ")
    with open("arrData.txt", "w+", encoding="utf-8") as f:
        f.write(str(x(arr)))
        f.close()
    print(len(arr))
    file.close()