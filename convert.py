import re

def filter_match(arr):
    for a in range(len(arr)):
        if a+1 < len(arr) and re.compile(r"(\w+) (\w+)").match("{} {}".format(arr[a], arr[a+1])):
            a1 = ''.join(r'[A-Za-z]' for x in arr[a])
            a2 = ''.join(r'[A-Za-z]' for x in arr[a+1])
            if re.match(a1, arr[a]) and re.match(a2, arr[a+1]):
                print(arr[a] + " " + arr[a+1])
                arr[a] = "{} {}".format(arr[a], arr[a+1])
                del arr[a+1]
            else: print("Not a match {} {}".format(arr[a], arr[a+1]))
    # return [i for i in arr if i]
    result = []
    tempArray = []
    arr = [i for i in arr if i]
    # TODO: Filter out -> N. (I.E. - 3. ) items
    for i in range(len(arr)):
        if len(tempArray) == 5:
            result.append(tempArray)
            tempArray = []
        elif len(tempArray) < 5:
            tempArray.append(arr[i])
    return result




with open("data.txt", "r", encoding="utf-8") as file:
    f = file.read()
    arr = f.split(" ")  
    with open("arrData.txt", "w+", encoding="utf-8") as f:
        f.write(str(filter_match(arr)))
        f.close()
    # print(len(arr))
    file.close() 