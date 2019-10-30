projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

lead_proj = list(zip(projects, leaders))

for p, l in lead_proj:
    print('The leader od ', p, ' is ', l)

print('-'*20)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for i, (p, l, d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1, p, d, l))

