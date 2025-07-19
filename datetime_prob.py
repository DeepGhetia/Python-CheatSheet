from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

lt = []
for i in range(1,13):
    start = f'01-{i}-2025'
    end = ((datetime.strptime(start, '%d-%m-%Y') + relativedelta(months=1)) - timedelta(days=1)).strftime('%d-%m-%Y')
    lt.append([start, end])

fianl_list = []
for i,j in lt:
    final = []
    for temp in range(int(i[:2]), int(j[:2])+1):
        s = str(temp)+i[2:]
        date_con = datetime.strptime(s,'%d-%m-%Y').strftime('%u')
        if date_con == '5':
            final.append((datetime.strptime(s,'%d-%m-%Y')).strftime('%d-%m-%Y'))
    fianl_list.append(final)
print([i[-1] for i in fianl_list])