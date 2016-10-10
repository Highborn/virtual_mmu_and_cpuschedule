from memory_management_algorithms import *
from utils import show_memory


def fit_process(process, m_table, word_length, algorithm):
    """
    :param process: process: a tuple with 'process name' as first value and 'process size' as second.
    :param m_table: a list with 2 lists, index 0 - memory block used( triad tuples: memory index, process name, size ).
                    and index 1 - free spaces in memory( dyadic lists: memory index, size ).
    :param word_length: word length of memory
    :param algorithm: 1 for FirstFit, 2 for BestFit and 3 for WorstFit.
    :return: fitted space in memory, a triad tuple with memory index, process name, and process size
    """
    fitted = ()
    if algorithm is 1:
        fitted = first_fit(process, m_table, word_length)
    elif algorithm is 2:
        fitted = best_fit(process, m_table, word_length)
    elif algorithm is 3:
        fitted = worst_fit(process, m_table, word_length)
    return fitted


def free_memory(p_name, m_table, word_length):
    """
    :param p_name: name of the process that is will be removed.
    :param m_table: a list with 2 lists, index 0 - memory block used( triad tuples: memory index, process name, size ).
                    and index 1 - free spaces in memory( dyadic lists: memory index, size ).
    :param word_length: word length of memory
    :return: nothing
    """
    new_free_space = [-1, 0]
    for item in m_table[0]:
        if item[1] == p_name:
            s_recovered = m_table[0].pop(m_table[0].index(item))
            new_free_space = [s_recovered[0], s_recovered[2]]
            unused_mem = word_length - (new_free_space[1] % word_length)
            if unused_mem is not word_length:
                new_free_space[1] += unused_mem
            print('{} removed.'.format(p_name))
    for item in m_table[1]:
        if item[0] + (item[1]//word_length) is new_free_space[0]:
            new_free_space[0] = item[0]
            new_free_space[1] += item[1]
            m_table[1].pop(m_table[1].index(item))
        elif new_free_space[0] + (new_free_space[1]//word_length) is item[0]:
            new_free_space[1] += item[1]
            m_table[1].pop(m_table[1].index(item))
    if new_free_space[0] is not -1:
        m_table[1].append(new_free_space)

    return


def memory_management_unit(m_table, word_length, algorithm):
    """
    :param m_table: a list with 2 lists, index 0 - memory block used( triad tuples: memory index, process name, size ).
                    and index 1 - free spaces in memory( dyadic lists: memory index, size ).
    :param word_length: word length of memory
    :param algorithm: 1 for FirstFit, 2 for BestFit, 3 for WorstFit, 0 for memory status.
    :return: nothing
    """
    if algorithm is 0:
        show_memory(m_table, word_length)
        return

    print(
        'input a process ...\n'
        '( e.g. : \'p1 256\' for a process with p1 as name and 256 bytes as memory need. )\n'
        'or free the space by a process ...\n'
        '( e.g. : \'rm p1\' for a process with p1, rm stands for remove. )\n'
    )
    while True:
        try:
            input_str = input()
            input_str = input_str.split()
            if input_str[0] == '0':
                show_memory(m_table, word_length)
            elif input_str[0] == 'rm':
                free_memory(input_str[1], m_table, word_length)
            else:
                process = (input_str[0], int(input_str[1]))
                fitted = fit_process(process, m_table, word_length, algorithm)
                print(fitted)

        except KeyboardInterrupt:
                print('\nKeyboardInterrupt.\n\n')
                break
    return
