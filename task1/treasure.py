arr = [[34,21,32,41,25],
       [14,42,43,14,31],
       [54,45,52,42,23],
       [33,15,51,31,35],
       [21,52,33,13,23]]
row = 1
col = 1
while True:
    row1 = row-1
    col1 = col-1
    value = arr[row1][col1]
    current = row * 10 + col
    print(value)
    if value == current:
            print(f"found at cell {row}, {col}")
            break
    row = value // 10
    col = value % 10