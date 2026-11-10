import numpy as np

def calculate(lists):
    final = np.array(lists).reshape(3, 3)
    
    mean_a0 = np.mean(final, axis = 0).tolist()
    mean_a1 = np.mean(final, axis = 1).tolist()
    mean_all = np.mean(final).tolist()
    var_a0 = np.var(final, axis = 0).tolist()
    var_a1 = np.var(final, axis = 1).tolist()
    var_all = np.var(final).tolist()
    std_a0 = np.std(final, axis = 0).tolist()
    std_a1 = np.std(final, axis = 1).tolist()
    std_all = np.std(final).tolist()
    max_a0 = np.max(final, axis = 0).tolist()
    max_a1 = np.max(final, axis = 1).tolist()
    max_all = np.max(final).tolist()
    min_a0 = np.min(final, axis = 0).tolist()
    min_a1 = np.min(final, axis = 1).tolist()
    min_all = np.min(final).tolist()
    sum_a0 = np.sum(final, axis = 0).tolist()
    sum_a1 = np.sum(final, axis = 1).tolist()
    sum_all = np.sum(final).tolist()

    calculation = {
        'mean': [mean_a0, mean_a1, mean_all],
        'variance': [var_a0, var_a1, var_all],
        'standard deviation': [std_a0, std_a1, std_all], 
        'max': [max_a0, max_a1, max_all], 
        'min': [min_a0, min_a1, min_all], 
        'sum': [sum_a0, sum_a1, sum_all]
    }

    return calculation

print(calculate([0,1,2,3,4,5,6,7,8]))
