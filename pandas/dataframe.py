import pandas as pd

celebrities = [
    ['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'],
    ['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'],
    ['Harry Potter', 'July 31, 1980', 'Wizard'],
    ['Ji-Sung Park', 'February 25, 1981', 'Footballer']
]

df = pd.DataFrame(celebrities, columns=['name', 'birthday', 'occupation'])
df # 테스트 코드
