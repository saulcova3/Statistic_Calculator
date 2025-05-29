import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)
    
    # Calculations for rows (axis=1), columns (axis=0), and flattened
    calculations = {
        'mean': [
            np.mean(matrix, axis=1).tolist(),  # Rows
            np.mean(matrix, axis=0).tolist(),  # Columns
            np.mean(matrix)                   # Flattened
        ],
        'variance': [
            np.var(matrix, axis=1).tolist(),   # Rows
            np.var(matrix, axis=0).tolist(),   # Columns
            np.var(matrix)                     # Flattened
        ],
        'standard deviation': [
            np.std(matrix, axis=1).tolist(),   # Rows
            np.std(matrix, axis=0).tolist(),   # Columns
            np.std(matrix)                     # Flattened
        ],
        'max': [
            np.max(matrix, axis=1).tolist(),   # Rows
            np.max(matrix, axis=0).tolist(),   # Columns
            np.max(matrix)                     # Flattened
        ],
        'min': [
            np.min(matrix, axis=1).tolist(),   # Rows
            np.min(matrix, axis=0).tolist(),   # Columns
            np.min(matrix)                     # Flattened
        ],
        'sum': [
            np.sum(matrix, axis=1).tolist(),   # Rows
            np.sum(matrix, axis=0).tolist(),   # Columns
            np.sum(matrix)                    # Flattened
        ]
    }
    
    return calculations