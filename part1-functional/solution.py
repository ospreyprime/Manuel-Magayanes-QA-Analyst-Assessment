def remove_duplicates(inputArray):
    # Create an array that doesn't display duplicates
    noDuplicatesArray = []
    # For-loop to check each number in the given array
    for number in inputArray:
        if number not in noDuplicatesArray:
            noDuplicatesArray.append(number)
    # Then return the array without duplicate values
    return noDuplicatesArray




if __name__== "__main__":
    case1 = remove_duplicates([1, 2, 3, 2, 4, 1, 5])
    case2 = remove_duplicates([1, 1, 1]) 
    case3 = remove_duplicates([])
    print(f"{case1}\n{case2}\n{case3}\n")