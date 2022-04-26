import cProfile


def alg1(n):
    """Первый алгоритм"""

    lst = []
    k = 0
    for i in range(2, n + 1):
        for j in lst:
            if i % j == 0:
                k += 1
                break
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst[len(lst) - 1]

# cProfile.run('alg1(100)')
# 30 function calls in 0.000 seconds
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 les_4_task_2.py:4(alg1)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# "les_4_task_2.alg1(10)"
# 1000 loops, best of 5: 2.47 usec per loop

# "les_4_task_2.alg1(20)"
# 1000 loops, best of 5: 5.42 usec per loop

# "les_4_task_2.alg1(100)"
# 1000 loops, best of 5: 36.1 usec per loop

# "les_4_task_2.alg1(500)"
# 1000 loops, best of 5: 353 usec per loop

# "les_4_task_2.alg1(1000)"
# 1000 loops, best of 5: 1.04 msec per loop


def alg2(n):
    """Второй алгоритм"""

    lst = list(range(n + 1))
    lst[1] = 0
    for i in lst:
        if i > 1:
            for j in range(i + i, len(lst), i):
                lst[j] = 0
    lst1 = [x for x in lst if x != 0]
    return lst1[len(lst1) - 1]


# cProfile.run('alg2(100)')
# 31 function calls in 0.000 seconds
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 les_4_task_2.py:45(alg2)
#  1    0.000    0.000    0.000    0.000 les_4_task_2.py:54(<listcomp>)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 26    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# "les_4_task_2.alg2(10)"
# 1000 loops, best of 5: 3.48 usec per loop

# "les_4_task_2.alg2(20)"
# 1000 loops, best of 5: 5.96 usec per loop

# "les_4_task_2.alg2(100)"
# 1000 loops, best of 5: 24.8 usec per loop

# "les_4_task_2.alg2(500)"
# 1000 loops, best of 5: 121 usec per loop

# "les_4_task_2.alg2(1000)"
# 1000 loops, best of 5: 244 usec per loop