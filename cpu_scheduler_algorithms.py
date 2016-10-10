def first_come_first_served(p_table):
    candidate = p_table[0]
    for process in p_table:
        if candidate.enter > process.enter:
            candidate = process
    return candidate


def priority(p_table):
    candidate = p_table[0]
    for process in p_table:
        if process.priority > candidate.priority:
            candidate = process
        elif process.priority == candidate.priority and candidate.enter > process.enter:
            candidate = process
    return candidate


def highest_response_ratio_next(p_table, c_time):
    candidate = p_table[0]
    hrr = (c_time - candidate.enter)/candidate.burst
    for process in p_table:
        rr = (c_time - process.enter)/process.burst
        if hrr < rr:
            candidate = process
            hrr = rr
    return candidate


def shortest_process_next(p_table):
    candidate = p_table[0]
    best_expected = burst_approx(candidate)
    for process in p_table:
        process_burst_approx = burst_approx(process)
        if best_expected > process_burst_approx:
            candidate = process
            best_expected = process_burst_approx
    return candidate


def burst_approx(process):
    approx = process.burst
    try:
        history = process.get('history')
        approx = 0
        count = 1
        length = len(history)
        for i in range(0, length-1):
            count /= 2
            approx += count * int(history[i])
        approx += count * int(history[length - 1])
    except IndexError:
        pass
    return approx


def shortest_remaining_time(p_table):
    candidate = p_table[0]
    for process in p_table:
        if candidate.burst > process.burst:
            candidate = process
    return candidate


def earliest_deadline_first(p_table):
    candidate = p_table[0]
    for process in p_table:
        if process.service + process.enter < candidate.service + candidate.enter:
            candidate = process
    return candidate


def rate_monotonic_scheduling(p_table):
    candidate = p_table[0]
    for process in p_table:
        if process.service < candidate.service:
            candidate = process
    return candidate

FCFS = first_come_first_served
HRRN = highest_response_ratio_next
SPN = shortest_process_next
SRT = shortest_remaining_time
EDF = earliest_deadline_first
RMS = rate_monotonic_scheduling
