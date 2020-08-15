def separate():
    with open("arrData.txt", "r", encoding="utf-8") as data:
        d = data.read()
        # print(d[0])
        index = 0
        tempArr = []
        result = []
        for i in range(len(d)):
            if index == 5:
                result.append(tempArr)
                # print(tempArr)
                tempArr = []
            if index <= 5:
                tempArr.append(d[i])
                index += 1


separate()
        