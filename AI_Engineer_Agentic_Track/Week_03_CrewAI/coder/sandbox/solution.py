# Calculate the first 1,000,000 terms of the series and multiply by 4

def calculate_series(terms):
    total = 0.0
    for i in range(terms):
        total += (-1)**i / (2 * i + 1)
    return total * 4

if __name__ == '__main__':
    result = calculate_series(1000000)
    print(result)