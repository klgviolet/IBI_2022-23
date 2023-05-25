import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/33356/IBI1_2022--23/IBI1_2022-23/practical7")
os.getcwd()
os.listdir()

covid_data = pd.read_csv("full_data.csv")

# showing the second column from every 100th row from the first 1000 rows 
first_1000 = covid_data.iloc[:1001]
print(first_1000.iloc[0::100, 1])

# used a Boolean to show “total cases” for all rows corresponding to Afghanistan
Afghanistan_cases = covid_data["location"] == "Afghanistan"
print('Boolean:', Afghanistan_cases)

# compute the mean number of new cases and new deaths on 31 March 2020
march_31_column = covid_data["date"] == "2020-03-31"
new_cases = covid_data.loc[march_31_column,'new_cases']
new_deaths = covid_data.loc[march_31_column,'new_deaths']
mean_new_cases = np.mean(new_cases)
mean_new_deaths = np.mean(new_deaths)
print('mean of new cases:',mean_new_cases,'mean of new deaths:',mean_new_deaths)


# create the boxplot 
plt.boxplot([new_cases,new_deaths])
plt.xticks(ticks=[1, 2], labels=["New Cases", "New Deaths"])
plt.ylabel("Number of Cases")
plt.title("New Cases and New Deaths on 31 March 2020")
plt.show()

# new cases and new deaths
world_data = covid_data[covid_data['location'] == 'World']
world_new_cases = world_data["new_cases"]
world_new_deaths = world_data["new_deaths"]
world_dates = world_data["date"]

plt.figure(figsize=(10,8))
plt.plot(world_dates, world_new_cases, 'b-',label='New Cases')
plt.plot(world_dates, world_new_deaths, 'r-',label='New Deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number of New cases/New deaths')
plt.title('New Cases and New Deaths Worldwide over Time')
plt.xticks(fontsize = 7)
plt.legend()
plt.show()

# Answer the question
UK_data = covid_data[covid_data['location'] == 'United Kingdom']
UK_new_cases = UK_data["new_cases"]
UK_total_cases = UK_data["total_cases"]
UK_dates = UK_data["date"]

plt.figure(figsize=(10,8))
plt.plot(UK_dates, UK_new_cases, 'b-',label='New Cases')
plt.plot(UK_dates, UK_total_cases, 'r-',label='Total Cases')
plt.xticks(UK_dates.iloc[0:len(UK_dates):3],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number of New cases/Total cases')
plt.title('New Cases and Total Cases Developed over Time in the UK')
plt.xticks(fontsize = 7)
plt.legend()
plt.show()
