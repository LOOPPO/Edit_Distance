import numpy as np

def edit_distance(x, y):
    m = len(x)
    n = len(y)
    delete_cost = 1
    insert_cost = 1
    twiddle_cost = 1
    replace_cost = 1
    copy_cost = 0
    c = np.zeros((m + 1, n + 1), int)
    op = np.zeros((m + 1, n + 1), str)
    for i in range(m + 1):
        c[i, 0] = i * delete_cost
        op[i, 0] = 'DELETE'
    for j in range(n + 1):
        c[0, j] = j * insert_cost
        op[0, j] = 'INSERT'
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i, j] = 99
            if x[i - 1] == y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + copy_cost
                op[i, j] = 'COPY'
            if x[i - 1] != y[j - 1] and (c[i - 1, j - 1] + replace_cost < c[i, j]):
                c[i, j] = c[i - 1, j - 1] + replace_cost
                op[i, j] = 'REPLACE'
            if i >= 2 and j >= 2 and x[i - 1] == y[j - 2] and x[i - 2] == y[j - 1] and c[i - 2, j - 2] + twiddle_cost < \
                    c[i, j]:
                c[i, j] = c[i - 2, j - 2] + twiddle_cost
                op[i, j] = 'TWIDDLE'
            if c[i - 1, j] + delete_cost < c[i, j]:
                c[i, j] = c[i - 1, j] + delete_cost
                op[i, j] = 'DELETE'
            if c[i, j - 1] + insert_cost < c[i, j]:
                c[i, j] = c[i, j - 1] + insert_cost
                op[i, j] = 'INSERT'
    return c[m,n]

def op_sequence(op, i, j):
    if i == 0 and j == 0:
        return
    if op[i, j] == 'C' or op[i, j] == 'R':
        i_n = i - 1
        j_n = j - 1
    elif op[i, j] == 'T':
        i_n = i - 2
        j_n = j - 2
    elif op[i, j] == 'D':
        i_n = i - 1
        j_n = j
    elif op[i, j] == 'INSERT':
        i_n = i
        j_n = j - 1
    op_sequence(op, i_n, j_n)
    print(op[i, j])