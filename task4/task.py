import numpy as np

def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator = np.sqrt(sum((x[i] - mean_x)**2 for i in range(len(x))) * sum((y[i] - mean_y)**2 for i in range(len(y))))

    if denominator == 0:
        return 0.0
    else:
        return numerator / denominator

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)