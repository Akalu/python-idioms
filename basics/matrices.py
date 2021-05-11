def traverse_2d_matrix():
    matrix2d = []
    n = 4
    m = 3
    for i in range(n):
        line = []
        val = i
        for j in range(m):
            line.append(val)
            val += 1
        matrix2d.append(line)

    print(matrix2d)
    print(matrix2d[0])
    print(matrix2d[1][2])


def traverse_2d_matrix_compr():
    n = 4
    m = 3
    matrix2d = [[0] * m for _ in range(n)]

    for i in range(n):
        val = i
        for j in range(m):
            matrix2d[i][j] = val
            val += 1

    print(matrix2d)
    print(matrix2d[0])
    print(matrix2d[1][2])


def main():
    traverse_2d_matrix()
    traverse_2d_matrix_compr()


if __name__ == '__main__':
    main()
