def fibonacci_iterative(n):
    series = [0, 1]  
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series[:n]

n = 10
print(fibonacci_iterative(n))  
