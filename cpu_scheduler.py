from cpu_scheduler_algorithms import *
from utils import Process
import time


def find_next_process(p_table, algorithm, current_time):
    """
    :param p_table: a list of processes - instances of class Process.
    :param algorithm: an integer in range [1,8].
    :param current_time: current time.
    :return: next process that must be dispatched on cpu.
    """
    next_process = p_table[0]
    if algorithm is 1:
        next_process = FCFS(p_table)
    elif algorithm is 2:
        next_process = HRRN(p_table, current_time)
    elif algorithm is 3:
        next_process = SPN(p_table)
    elif algorithm is 4 or 5:
        next_process = priority(p_table)
    elif algorithm is 6:
        next_process = SRT(p_table)
    elif algorithm is 7:
        next_process = EDF(p_table)
    elif algorithm is 8:
        next_process = RMS(p_table)
    return next_process


def cpu_scheduler(p_table, algorithm):
    """
    :param p_table: a list of processes - instances of class Process.
    :param algorithm: an integer in range [1,8].
    :return: next process that must be dispatched on cpu.
    """
    current_time = 0
    current_p_table = []
    enter_times = [99999]
    preemptive = (5, 6, 7, 8)
    non_preemptive = (1, 2, 3, 4)
    real_time = (7, 8)

    for process in p_table:
        if process.enter not in enter_times:
            enter_times.append(process.enter)
    enter_times.sort(reverse=True)
    next_entrance = enter_times.pop()

    while len(p_table) is not 0:
        for process in p_table:
            if process not in current_p_table:
                if process.enter <= current_time:
                    current_p_table.append(process)

        next_process = find_next_process(p_table, algorithm, current_time)
        print('{} : process {} is running'.format(current_time, next_process.name))
        if algorithm in real_time:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print('\nKeyboardInterrupt.')
                break

        if algorithm in non_preemptive:
            p_table.pop(p_table.index(next_process))
            current_time += next_process.burst
            print('{} : ...terminated'.format(current_time))

        elif algorithm in preemptive:
            if current_time >= next_entrance:
                next_entrance = enter_times.pop()
            burst_time = (next_entrance - current_time)
            if burst_time < next_process.burst:
                next_process.burst -= burst_time
                current_time = next_entrance
            else:
                process = p_table.pop(p_table.index(next_process))
                if algorithm in real_time:
                    new_process = Process(process.name, process.enter, process.service, process.burst)
                    new_process.enter += process.service
                    p_table.append(new_process)
                    if new_process.enter not in enter_times:
                        enter_times.append(new_process.enter)
                        enter_times.sort(reverse=True)
                current_time += next_process.burst
                print('{} : ...terminated'.format(current_time))

        else:
            raise ValueError('The entered value is not in defined range')

    print('\n')

    return
