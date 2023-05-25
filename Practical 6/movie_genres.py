import matplotlib.pyplot as plt
genres = {'Comedy': 73,
          'Action': 42,
          'Romance': 38,
          'Fantasy': 28,
          'Science-fiction': 22,
          'Horror': 19,
          'Crime': 18,
          'Documentary': 12,
          'History': 8,
          'War': 7,
}
print(genres)
plt.pie(genres.values(), labels=genres.keys(), autopct='%1.1f%%')
plt.title('Movie genres')
plt.show()
var = 'Comedy'                      #  A variable for the typical genre
print(genres[var])   # print the number
