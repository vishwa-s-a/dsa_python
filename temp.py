# Create an empty 2D list (matrix)
matrix = []

# Define the dimensions of the matrix (rows and columns)
rows = 3
columns = 4

# Initialize the matrix with zeros or any default value
for _ in range(rows):
    matrix.append([0] * columns)

# Display the initial matrix
print("Initial Matrix:")
for row in matrix:
    print(row)

# Add values to the matrix
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = i * columns + j + 1

# Display the matrix after adding values
print("\nMatrix After Adding Values:")
for row in matrix:
    print(row)
