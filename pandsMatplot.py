import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# convert the file from excel to csv just firstOne with pip install xlrd

'''
#covid19_xlsx = pd.read_excel("covid19.xlsx")
#covid19_xlsx.to_csv('covid19.csv')'''

covid19_csv = pd.read_csv("covid19.csv")
#print(covid19_csv)
covid19_csv1 = pd.DataFrame(covid19_csv)
covid19_continent = covid19_csv1[['continent', 'location', 'date', 'total_cases', 'total_deaths']]
#print(covid19_continent)
covid19_continent = covid19_continent.set_index('continent', 'location')

europe_covid19 = covid19_continent.loc[(covid19_continent['location'] == 'Italy') | (covid19_continent['location'] == 'Germany') |
                                       (covid19_continent['location'] == 'Albania') | (covid19_continent['location'] == 'Greece')]
#print(europe_covid19)
