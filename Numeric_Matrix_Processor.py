def add_mx():
    a_matrix_row, a_matrix_columns = input("Enter size of first matrix: ").split()
    a_matrix = []
    print("Enter first matrix:")
    for row in range(1, int(a_matrix_row) + 1):
        a_matrix.append(input().split(" "))

    b_matrix_row,  b_matrix_columns = input("Enter size of second matrix: ").split()
    b_matrix = []
    print("Enter second matrix:")
    for row in range(1,int(b_matrix_row) + 1):
        b_matrix.append(input().split(" "))

    a_plus_b = []

    if a_matrix_row != b_matrix_row or a_matrix_columns != b_matrix_columns:
        print("ERROR")
    else:
        print("The result is:")
        for row in range(0,int(a_matrix_row)):
            a_plus_b.append([])
            for column in range(0,int(a_matrix_columns)):
                a_plus_b[row].append(float(a_matrix[row][column]) + float(b_matrix[row][column]))
        for row in range(int(a_matrix_row)):
            print(*a_plus_b[row])
        print("")
        menu()


def multiply_mx_by_constatnt():
    a_matrix_row,  a_matrix_columns = input("Enter size of matrix: ").split()
    a_matrix = []

    print("Enter matrix: ")
    for row in range(1,int(a_matrix_row) + 1):
        a_matrix.append(input().split(" "))

    b = input("Enter constant: ")

    a_multiplicated_by_constant = []

    for row in range(0,int(a_matrix_row)):
        a_multiplicated_by_constant.append([])
        for column in range(0,int(a_matrix_columns)):
                a_multiplicated_by_constant[row].append(float(a_matrix[row][column]) * float(b))
    print("The result is:")
    for row in range(int(a_matrix_row)):
        print(*a_multiplicated_by_constant[row])
    print("")
    menu()


def multiply_mx():
    a_matrix_row, a_matrix_columns = input("Enter size of first matrix: ").split()
    a_matrix = []
    print("Enter first matrix:")
    for row in range(1, int(a_matrix_row) + 1):
        a_matrix.append(input().split(" "))

    b_matrix_row,  b_matrix_columns = input("Enter size of second matrix: ").split()
    b_matrix = []
    print("Enter second matrix:")
    for row in range(1,int(b_matrix_row) + 1):
        b_matrix.append(input().split(" "))

    a_multi_mx_b = []

    if a_matrix_columns != b_matrix_row:
        print("ERROR")
    else:
        print("The result is:")
        for row_a in range(0, int(a_matrix_row)):
            a_multi_mx_b.append([])
            a_row_to_multiply = []
            for a1 in a_matrix[row_a]:
                a_row_to_multiply.append(float(a1))
            for column_b in range(0, int(b_matrix_columns)):
                b_column_to_multiply = []
                for row_b in range(0, int(b_matrix_row)):
                    b_column_to_multiply.append(float(b_matrix[row_b][column_b]))
                final_poz = 0
                for poz in range(0, int(a_matrix_columns)):
                    final_poz += a_row_to_multiply[poz] * b_column_to_multiply[poz]
                a_multi_mx_b[row_a].append(final_poz)
        for row in a_multi_mx_b:
            print(*row)
        print("")
        menu()

def transpose():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    choice = input("Your choice: ")
    matrix_row, matrix_columns = input("Enter matrix size:").split()
    matrix = []
    print("Enter matrix:")
    for row in range(1, int(matrix_row) + 1):
        matrix.append(input().split(" "))
    print("The result is:")
    if choice == "1":
        transposed_mx = []
        for column in range(0, int(matrix_columns)):
            transposed_mx.append([])
            for row in range(0, int(matrix_row)):
                transposed_mx[column].append(matrix[row][column])
        for row in transposed_mx:
            print(*row)
    elif choice == "2":
        transposed_mx = []
        i = 0
        for column in reversed(range(0, int(matrix_columns))):
            transposed_mx.append([])
            for row in reversed(range(0, int(matrix_row))):
                transposed_mx[i].append(matrix[row][column])
            i += 1
        for row in transposed_mx:
            print(*row)
    elif choice == "3":
        transposed_mx = []
        for row in range(0, int(matrix_row)):
            transposed_mx.append([])
            for column in reversed(range(0, int(matrix_columns))):
                transposed_mx[row].append(matrix[row][column])
        for row in transposed_mx:
            print(*row)
    elif choice == "4":
        transposed_mx = []
        i = 0
        for row in reversed(range(0, int(matrix_row))):
            transposed_mx.append([])
            for column in range(0, int(matrix_columns)):
                transposed_mx[i].append(matrix[row][column])
            i += 1
        for row in transposed_mx:
            print(*row)
    print("")
    menu()


def determinant():
    matrix_row, matrix_columns = input("Enter matrix size:").split()
    matrix = []
    print("Enter matrix: ")
    for row in range(1, int(matrix_row) + 1):
        matrix.append(input().split(" "))
    print("The result is:")
    print(determinant1(matrix))


def determinant1(matrix):
    if len(matrix) == 1:
        return float(matrix[0][0])
    elif len(matrix) == 2:
        return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
    else:
        det = 0
        for i in range(len(matrix)):
            minor = []
            for j in range(len(matrix)):
                if j != i:
                    minor.append(matrix[j][1:])
            det += ((-1) ** i) * float(matrix[i][0]) * determinant1(minor)
    return det


def inverse():
    matrix_row, matrix_columns = input("Enter matrix size:").split()
    matrix = []
    print("Enter matrix:")
    for row in range(1, int(matrix_row) + 1):
        matrix.append(input().split(" "))
    print("The result is:")
    transposed_mx = []
    for column in range(0, int(matrix_columns)):
        transposed_mx.append([])
        for row in range(0, int(matrix_row)):
            transposed_mx[column].append(mx_d(matrix)[row][column])
    det = 1/determinant1(matrix)

    a_multiplicated_by_constant = []
    for row in range(len(transposed_mx)):
        a_multiplicated_by_constant.append([])
        for column in range(len(transposed_mx)):
            a_multiplicated_by_constant[row].append(round(float(transposed_mx[row][column]) * det, 3))
    for row in range(int(matrix_row)):
        print(*a_multiplicated_by_constant[row])
    print("")
    menu()


def mx_d(matrix):
    global det_mx, matrix_d
    matrix_d = []
    for i in range(len(matrix)):
        matrix_d.append([])
        for j in range(len(matrix)):
            det_mx = []
            row = 0
            for ai in range(len(matrix)):
                if ai != i:
                    det_mx.append([])
                    for aj in range(len(matrix)):
                        if aj != j:
                            det_mx[row].append(matrix[ai][aj])
                    row += 1
            matrix_d[i].append(((-1) ** (i+j)) * determinant1(det_mx))
    return matrix_d


def menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice = input("Your choice: ")
    if choice == "0":
        return False
    else:
        if choice == "1":
            add_mx()
        elif choice == "2":
            multiply_mx_by_constatnt()
        elif choice == "3":
            multiply_mx()
        elif choice == "4":
            transpose()
        elif choice == "5":
            determinant()
        elif choice == "6":
            inverse()
menu()
