import os


class Process:
    def __init__(self, name, enter, service, burst, priority=0, **kwargs):
        self.name = name
        self.enter = enter
        self.service = service
        self.burst = burst
        self.priority = priority
        self.variables = kwargs

    def set(self, var, val):
        self.variables[var] = val

    def get(self, var):
        return self.variables.get(var, None)

    def print(self):
        print(self.name, self.enter, self.service, self.burst, self.priority)


def job_scheduler(file_name='input'):
    input_file = open(file_name)
    table = []
    for line in input_file:
        line.replace('\n', '')
        attributes, history = line.split(sep='H')
        attributes = attributes.split()
        process = Process(
                attributes[0],
                int(attributes[1]),
                int(attributes[2]),
                int(attributes[3]),
                int(attributes[4])
            )
        process.set('history', history.split())
        table.append(process)

    return table


def editor():
    os.system('nano input')
    return


def memory_install():
    size = int(input('enter memory capacity in bytes : '))
    word_length = int(input('enter word length of memory in bytes : '))
    free_spaces = [[0, size]]
    used_spaces = []
    m_table = [used_spaces, free_spaces]
    print('memory has been installed.')

    return m_table, word_length


def show_memory(m_table, word_length=4):
    all_memory = []
    all_memory.extend(m_table[0])
    all_memory.extend(m_table[1])
    all_memory.sort(key=lambda x: x[0])
    for item in all_memory:
        if isinstance(item, tuple):
            size = item[2] + word_length - 1
            size //= word_length
            print('|====|', item[0], item[1])
            for i in range(1, size):
                print('|====|')
        else:
            size = item[1] + word_length - 1
            size //= word_length
            print('|    |', item[0])
            for i in range(1, size):
                print('|    |')
    print('\n')

    return
