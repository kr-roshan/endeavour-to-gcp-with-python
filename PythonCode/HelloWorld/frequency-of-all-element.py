# program to find the frequency of all element in a list in sequence.

def findFreqency(inputList):
    frequencyDict = {}
    for element in inputList:
        if element in frequencyDict:
            frequencyDict[element] += 1
        else:
            frequencyDict[element] = 1

    return frequencyDict

if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 9, 2, 9, 5, 6, 3, 7, 8, 7] * 3 # Repeat the list 3 times
    input_list.sort()
    # if you don't want to modify input list, sorted() function can also be used
    frequencyofAll = findFreqency(input_list)

    print(f"Input list: {input_list}")
    print("Frequency of the elements are")
    for element, frequency in frequencyofAll.items():
        print(f"{element} : {frequency}")

