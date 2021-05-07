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


def main():
    traverse_2d_matrix()


if __name__ == '__main__':
    main()
