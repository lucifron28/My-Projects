def get_int(x):
    while True:
        try:
            user_input = int(input(x))
        except ValueError:
            print("Invalid input.")
            print("Please enter a number.")
        else:
            return user_input
        

def main():    
    n = int(input("Enter matrix number: "))
    matrix = [[0] * n for _ in range(n)]

    left_col, right_col = 0, n - 1
    top_row, bottom_row = 0, n - 1
    value = 1

    while left_col <= right_col:
        for col in range(left_col, right_col + 1):
            matrix[top_row][col] = value
            value += 1
        top_row += 1

        for row in range(top_row, bottom_row + 1):
            matrix[row][right_col] = value
            value += 1
        right_col -= 1

        for col in range(right_col, left_col - 1, -1):
            matrix[bottom_row][col] = value
            value += 1
        bottom_row -= 1

        for row in range(bottom_row, top_row - 1, -1):
            matrix[row][left_col] = value
            value += 1
        left_col += 1

    max_value = n * n
    width = len(str(max_value))

    for row in matrix:
        for i in row:
            print(f"{i:>{width}}", end=' ')
        print()

if __name__ == '__main__':
    main()