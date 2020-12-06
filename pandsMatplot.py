import pandas as pd
import matplotlib.pyplot as plt


# convert the file from excel to csv just firstOne with pip install xlrd

'''
#covid19_xlsx = pd.read_excel("covid19.xlsx")
#covid19_xlsx.to_csv('covid19.csv')'''

covid19_csv = pd.read_csv("covid19.csv")
# print(covid19_csv)
covid19_csv1 = pd.DataFrame(covid19_csv)
covid19_continent = covid19_csv1[['continent', 'location', 'date', 'total_cases']]
# print(covid19_continent)

# choose Europe continent
covid19_europe = covid19_continent[covid19_continent['continent'] == 'Europe']
covid19_europe = pd.DataFrame(covid19_europe)
# date to datetime format
covid19_europe['date'] = pd.to_datetime(covid19_europe['date'], infer_datetime_format=True)

# print(covid19_europe)

covid19_europe.fillna(value=0, inplace=True)

# choose european countries
covid19_italy = covid19_europe[covid19_europe['location'] == 'Italy']
covid19_germany = covid19_europe[covid19_europe['location'] == 'Germany']
covid19_albania = covid19_europe[covid19_europe['location'] == 'Albania']
covid19_greece = covid19_europe[covid19_europe['location'] == 'Greece']
covid19_denmark = covid19_europe[covid19_europe['location'] == 'Denmark']
covid19_france = covid19_europe[covid19_europe['location'] == 'France']

countries_data = {"Italy": covid19_italy, "Germany": covid19_germany, "Albania": covid19_albania,
                  "Greece": covid19_greece, "Denmark": covid19_denmark, "France": covid19_france}

colors = {"Italy": "green", "Germany": "orange", "Albania": "yellow", "Greece": "blue", "Denmark": "red",
          "France": "purple"}

# Plot
plt.figure(figsize=(12, 8))
for country in countries_data:
    plt.plot(countries_data[country]["date"], countries_data[country]["total_cases"], color=colors[country],
             linewidth=2.5)
plt.legend(colors)
plt.ylabel('Total Cases')
plt.xlabel('Per Month \n Countries do not always release Figer every day, which may explain some of the sharp changes '
           'in the trendiness')
plt.title('Coronavirues cases increasing in European Countries in recent months')
plt.show()
