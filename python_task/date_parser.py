from datetime import datetime
from itertools import permutations

INPUT_FILE = 'input.txt'
DATE_MIN = datetime.strptime('2000/1/1', '%Y/%m/%d').date()
DATE_MAX = datetime.strptime('2999/12/31', '%Y/%m/%d').date()


def parse_date():
    
    try:
        with open(INPUT_FILE, 'r') as f:        
            input_str = f.read().strip()
    except FileNotFoundError:
        print('Input file {} not found.'.format(INPUT_FILE))
        return
        
    elements = input_str.split('/')
    
    if len(elements) < 3 or any(map(lambda x: not x.isdigit(), elements)):
        print(input_str + ' is illegal')
        return
        
    elements = sorted(elements, key=len)
    
    valid_dates = []
    
    if len(elements[-1]) == 4:  # year with century
        year = elements[-1]
        for month, day in permutations(elements[:-1]):
            try:
                this_date = datetime.strptime('{}/{}/{}'.format(year, month, day), '%Y/%m/%d').date()
                # print(this_date)
                if DATE_MIN <= this_date <= DATE_MAX:
                    valid_dates.append(this_date)
            except ValueError:
                continue    
    else:  # year as 1 or 2 digits
        for year, month, day in permutations(elements):
            year = '20' + year.rjust(2, '0')
            try:
                this_date = datetime.strptime('{}/{}/{}'.format(year, month, day), '%Y/%m/%d').date()
                # print(this_date)
                if DATE_MIN <= this_date <= DATE_MAX:
                    valid_dates.append(this_date)
            except ValueError:
                continue
            
    if len(valid_dates) == 0:
        print(input_str + ' is illegal')
        return
        
    valid_dates.sort()
    # print(valid_dates)
    
    print(valid_dates[0].strftime('%Y-%m-%d'))


if __name__ == '__main__':
    
    parse_date()
        
