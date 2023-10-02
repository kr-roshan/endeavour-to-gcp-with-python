# program to find the frequency of an element in a list.

def findFrequency(element, list):
    count = 0
    for item in list:
        if item == element:
            count += 1

    return count;


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 9, 2, 9, 5, 6, 3, 7, 8, 7] * 3 # Repeat the list 3 times

    element = 7
    frequency = findFrequency(element, input_list)

    print(f"The frequency of {element} is {frequency}")


