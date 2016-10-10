#!/usr/bin/python3
from utils import *
import cpu_scheduler as cs
import memory_management as mm


if __name__ == '__main__':
    while True:
        x = input(
            'Enter one of the following codes ...\n'
            '\'0\' : edit input file(requires unix like OS.).\n'
            '\'1\' : cpu scheduling algorithms.\n'
            '\'2\' : memory management algorithms.\n'
            '\'9\' : exit.\n'
        )
        if x == '0':
            editor()
        if x == '1':
            p_table = job_scheduler()
            x = int(input(
                'Enter one of the following codes ...\n'
                '\'1\' : FCFS.\n'
                '\'2\' : HRRN.\n'
                '\'3\' : SPN.\n'
                '\'4\' : Priority.\n'
                '\'5\' : Priority(preemptive).\n'
                '\'6\' : SRT.\n'
                '\'7\' : EDF.\n'
                '\'8\' : RMS.\n'
            ))
            cs.cpu_scheduler(p_table, x)
        if x == '2':
            try:
                m_table
                x = input('would you mind to reinstall memory? ( N/y ) ')
            except NameError:
                x = 'y'
            if x == 'y':
                m_table, word_len = memory_install()
            x = int(input(
                'Enter one of the following codes ...\n'
                '\'1\' : First Fit.\n'
                '\'2\' : Best Fit.\n'
                '\'3\' : Worst Fit.\n'
                '\'0\' : See the current status of memory.\n'
            ))
            mm.memory_management_unit(m_table, word_len, x)
        if x == '9':
            break
