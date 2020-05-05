# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

def profit_avg():
    org = namedtuple('New_Company', 'name q1 q2 q3 q4')
    org_dict = {}
    N = int(input('How many companies there will be? '))

    for i in range(N):
        New_Company = org(input('enter a name: ').title(),
                          int(input('q1 profit: ')),
                          int(input('q2 profit: ')),
                          int(input('q3 profit: ')),
                          int(input('q4 profit: ')))
        org_dict.update({New_Company.name:
                             (New_Company.q1 +
                              New_Company.q2 +
                              New_Company.q3 +
                              New_Company.q4)})

    avg_profit = sum(org_dict.values()) / len(org_dict)
    print(f'Average profit = {avg_profit:.2f}')

    for comp_name, year_profit in org_dict.items():
        if year_profit > avg_profit:
            print(f'{comp_name} year profit {year_profit} is above the avg {avg_profit:.2f}')
        elif year_profit < avg_profit:
            print(f'{comp_name} year profit {year_profit} is below the avg {avg_profit:.2f}')

print(profit_avg())


