import matplotlib.pyplot as plt
# create a list which contains the cost of these Olympic games
costs=[1,8,15,7,5,14,43,40]
# make the list sorted
sorted_costs = sorted(costs)
# create a list which contains Olympic games recent years
Olympic_Games = ['Los Angeles 1984',
                      'Seoul 1988',
                      'Barcelona 1992',
                      'Atlanta 1996',
                      'Sydney 2000',
                      'Athens 2003',
                      'Beijing 2008',
                      'London 2012']

print(sorted_costs)
plt.figure(figsize=(12,8))
plt.bar(Olympic_Games,sorted_costs,color = 'yellow')
plt.xticks(fontsize = 8)
plt.xlabel('Olympic Games', color = "red")
plt.ylabel('costs', color = "red")
plt.grid(True)
plt.show()
