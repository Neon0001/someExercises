def plusMinus(arr):
    positive = 0
    negativeRatio = 0
    zero = 0

    for numbers in arr:
        positive += numbers > 0
        negativeRatio += numbers < 0
        zero += numbers == 0

    arr_length = len(arr)

    positiveF = positive / arr_length
    negativeF = negativeRatio / arr_length
    zeroF = zero / arr_length

    print("{:.6f}".format(positiveF) + "\n" + "{:.6f}".format(negativeF) + "\n" + "{:.6f}".format(zeroF))


plusMinus([2, 4, 5, 2, 5, 2, -2, -3, -4, 0, 0, 0])
