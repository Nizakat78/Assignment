def main():
    numbers : list[int]=[1,2,3,4,5,6,7,8,9,10]

    for i  in range(len(numbers)):
        each_number_multiple_by_2 = numbers[i]
        numbers[i] = each_number_multiple_by_2 * 2
    
    print(f"Here is List of numbers which  multiple by 2 {numbers}")


main()