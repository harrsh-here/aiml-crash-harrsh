# Uses built-in enumerate tracking to automatically generate a numbered list iteration from a skills array.


skills = ['Python', 'Pandas', 'EDA', 'SQL', 'Numpy']
i=1
for s in skills:
    print(f'{i}. {s}')
    i+=1
for i,s in enumerate(skills):
    print(f'{i+1}. {s}')