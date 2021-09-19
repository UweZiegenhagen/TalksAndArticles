from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
from pprint import pprint

def prep_Cal(year, month):
    first = date(year, month, 1)
    last = first + relativedelta(months=+1, seconds=-1)
    month = []
    for i in range(5):
        month.append(['  ' for i in range(7)])

    if last.weekday() < 3:
        month.append(['  ' for i in range(7)])        

    week_counter = 0    
    daterange = pd.date_range(first, last)

    for i in daterange:
        weekday_before = (i + relativedelta(days=-1)).weekday()
        if i.weekday() > weekday_before:
            month[week_counter][i.weekday()] = str(i.day).zfill(2)
        else:
            week_counter = week_counter + 1    
            month[week_counter][i.weekday()] = str(i.day).zfill(2)
    return month

def as_table(month):
    print(r'\begin{tabular}{ccccccc}')
    print(r'Mo & Di & Mi & Do & Fr & Sa & So \\')
    for week in month:
        print(' & '.join(week), r'\\')
    print(r'\end{tabular}')

def as_tikz_table(month):
    for cntw, week in enumerate(month):
        for cntd, day in enumerate(week):
            print(f'\\node at ({cntd},{-cntw}) {{{day}}};')

def as_tikz_table_wknd(month):
    for cntw, week in enumerate(month):
        for cntd, day in enumerate(week):
            stil = '[wknd]' if cntd in [5,6] and \
            day != '  ' else ''
            print(f'\\node {stil} at ({cntd},{-cntw}) {{{day}}};')


september = prep_Cal(2021,9)
pprint(september)
as_tikz_table(september)
as_tikz_table_wknd(september)
