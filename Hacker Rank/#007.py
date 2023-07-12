if __name__ == '__main__':
    n = int(input())
    numbers = []
    
    for i in range(1, n + 1):
        numbers.append(str(i))
    
    result = ''.join(numbers)
    
    print(result)