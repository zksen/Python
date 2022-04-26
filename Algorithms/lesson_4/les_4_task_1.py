"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков."""


# Отдельно записал списки, чтобы не испортить чистоту эксперимента рандомным созданием списка
# В данной выборке списки длинной: 10, 20, 100, 500, 1000 соответственно
import cProfile
import lists


def rev1(l):
    """Первый алгоритм"""

    max_item = l[0]
    max_item_idx = 0
    min_item = l[0]
    min_item_idx = 0

    for i in range(len(l)):

        if max_item <= l[i]:
            max_item = l[i]
            max_item_idx = i

        if min_item >= l[i]:
            min_item = l[i]
            min_item_idx = i

    l[min_item_idx], l[max_item_idx] = l[max_item_idx], l[min_item_idx]


# cProfile.run('rev1(lists.my_list10)')
# 5 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:11(rev1)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# "les_4_task_1.rev1(lists.my_list10)"
# 1000 loops, best of 5: 2.21 usec per loop

# "les_4_task_1.rev1(lists.my_list20)"
# 1000 loops, best of 5: 3.34 usec per loop

# "les_4_task_1.rev1(lists.my_list100)"
# 1000 loops, best of 5: 13.4 usec per loop

# "les_4_task_1.rev1(lists.my_list500)"
# 1000 loops, best of 5: 67.5 usec per loop

# "les_4_task_1.rev1(lists.my_list1000)"
# 1000 loops, best of 5: 133 usec per loop


def rev2(l):
    """Второй алгоритм"""

    l1 = l[:]
    l.sort()
    l1[l1.index(l[0])], l1[l1.index(l[len(l) - 1])] = l1[l1.index(l[len(l) - 1])], l1[l1.index(l[0])]


# cProfile.run('rev2(lists.my_list10)')
# 11 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:64(rev2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}


# "les_4_task_1.rev2(lists.my_list10)"
# 1000 loops, best of 5: 1.12 usec per loop

# "les_4_task_1.rev2(lists.my_list20)"
# 1000 loops, best of 5: 1.29 usec per loop

# "les_4_task_1.rev2(lists.my_list100)"
# 1000 loops, best of 5: 3.26 usec per loop

# "les_4_task_1.rev2(lists.my_list500)"
# 1000 loops, best of 5: 12.6 usec per loop

# "les_4_task_1.rev2(lists.my_list1000)"
# 1000 loops, best of 5: 24.9 usec per loop


def rev3(l):
    """Третий алгоритм"""

    l[l.index(min(l))], l[l.index(max(l))] = l[l.index(max(l))], l[l.index(min(l))]


# cProfile.run('rev3(lists.my_list10)')
# 12 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:92(rev3)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
# 2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# "les_4_task_1.rev3(lists.my_list10)"
# 1000 loops, best of 5: 1.71 usec per loop

# "les_4_task_1.rev3(lists.my_list20)"
# 1000 loops, best of 5: 2.37 usec per loop

# "les_4_task_1.rev3(lists.my_list100)"
# 1000 loops, best of 5: 8.31 usec per loop

# "les_4_task_1.rev3(lists.my_list500)"
# 1000 loops, best of 5: 48.6 usec per loop

# "les_4_task_1.rev3(lists.my_list1000)"
# 1000 loops, best of 5: 92.2 usec per loop




# Вывод: самым оптимальным оказался второй алгоритм, потому что время работы его не растет линейно
# как в двух остальных.