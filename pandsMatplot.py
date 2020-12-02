import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# convert the file from excel to csv just firstOne with pip install xlrd

'''
#covid19_xlsx = pd.read_excel("covid19.xlsx")
#covid19_xlsx.to_csv('covid19.csv')'''

covid19_csv = pd.read_csv("covid19.csv")
#print(covid19_csv)

covid19_continent = covid19_csv[['continent','location','date','total_cases','total_deaths']]
#print(covid19_continent)
covid19_continent = covid19_continent.set_index('continent', 'location')
europe_covid19 = covid19_continent.loc[['Europe'], ['location','date','total_cases','total_deaths']]
#print(europe_covid19)

#'Italy','Germany','Albania','Greece'


