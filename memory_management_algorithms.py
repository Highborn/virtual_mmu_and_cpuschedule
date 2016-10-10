def first_fit(process, m_table, word_length):
    """
    :param process: a tuple with 'process name' as first value and 'process size' as second.
    :param m_table: a list with 2 lists, index 0 - memory block used( triad tuples: memory index, process name, size ).
                    and index 1 - free spaces in memory( dyadic lists: memory index, size ).
    :param word_length: word length of memory
    :return: a tuple which has the memory index, process name and its size.
    """
    fitted = (-1,)
    for free_space in m_table[1]:
        if free_space[1] >= process[1]:
            fitted = (
                free_space[0],  # memory index
                process[0],  # process name
                process[1],  # memory used by process
            )
            if process[1] % word_length is 0:
                free_space[0] += process[1] // word_length
                free_space[1] -= process[1]
            else:
                free_space[0] += (process[1] // word_length) + 1
                free_space[1] -= process[1] + word_length - (process[1] % word_length)
            if free_space[1] == 0:
                m_table[1].pop(m_table[1].index(free_space))
            break
    if fitted[0] is -1:
        fitted = 'can not fit this process in memory right now!'
    else:
        m_table[0].append(fitted)

    return fitted


def best_fit(process, m_table, word_length):
    """
    :param process: a tuple with 'process name' as first value and 'process size' as second.
    :param m_table: a list with 2 lists, index 0 - memory block used( triad tuples: memory index, process name, size ).
                    and index 1 - free spaces in memory( dyadic lists: memory index, size ).
    :param word_length: word length of memory
    :return: a tuple which has the memory index, process name and its size.
    """
    # fitted = ()
    candidate = [-1, 99999]
    for free_space in m_table[1]:
        if free_space[1] >= process[1]:
            if free_space[1] < candidate[1]:
                candidate = free_space
    if candidate[0] is -1:
        fitted = 'can not fit this process in memory right now!'
    else:
        fitted = (
            candidate[0],  # memory index
            process[0],  # process name
            process[1],  # memory used by process
        )
        if process[1] % word_length is 0:
            candidate[0] += process[1] // word_length
            candidate[1] -= process[1]
        else:
            candidate[0] += (process[1] // word_length) + 1
            candidate[1] -= process[1] + word_length - (process[1] % word_length)
        if candidate[1] == 0:
            m_table[1].pop(m_table[1].index(candidate))
        m_table[0].append(fitted)

    return fitted


def worst_fit(process, m_table, word_length):
    """
    :param process: a tuple with 'process name' as first value and 'process size' as second.
    :param m_table: a list with 2 lists, index 0 - memory block used( triad tuples: memory index, process name, size ).
                    and index 1 - free spaces in memory( dyadic lists: memory index, size ).
    :param word_length: word length of memory
    :return: a tuple which has the memory index, process name and its size.
    """
    # fitted = ()
    candidate = [-1, 0]
    for free_space in m_table[1]:
        if free_space[1] >= process[1]:
            if free_space[1] > candidate[1]:
                candidate = free_space
    if candidate[0] is -1:
        fitted = 'can not fit this process in memory right now!'
    else:
        fitted = (
            candidate[0],  # memory index
            process[0],  # process name
            process[1],  # memory used by process
        )
        if process[1] % word_length is 0:
            candidate[0] += process[1] // word_length
            candidate[1] -= process[1]
        else:
            candidate[0] += (process[1] // word_length) + 1
            candidate[1] -= process[1] + word_length - (process[1] % word_length)
        if candidate[1] == 0:
            m_table[1].pop(m_table[1].index(candidate))
        m_table[0].append(fitted)

    return fitted
