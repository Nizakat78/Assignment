def serious_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return[0]
    elif n == 2:
        return[0, 1]
    else:
       sequence = serious_fibonacci(n -1)
       sequence.append(sequence[-1] + sequence[-2])
       return sequence
print(serious_fibonacci(20))
