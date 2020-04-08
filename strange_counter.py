def strangeCounter(t):
    time = 1
    initialValue = 3
    tempValue = initialValue

    while (time < t):

        prevTime_Value = initialValue
        prevTime = time
        time = time + (tempValue - 1)
        if(time >= t):
            break
        prevTime_Value = initialValue
        initialValue = initialValue * 2
        tempValue = initialValue
        time += 1
        prevTime_Value = initialValue
        prevTime = time

    if (time == 1):
        return 3

    tDifference = t - prevTime
    tval = prevTime_Value - tDifference

    # print(str(prevTime)+ ' ' +str(prevTime_Value) + ' ' +str(time) + ' ' + str(tempValue))
    # print('t val = ' + str(tval))

    return tval


t = 1       #99999997668
result = strangeCounter(t)
print(result)
