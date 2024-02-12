# import matplotlib

import matplotlib

import matplotlib.pyplot as plt

months = [1,2,3,4,5,6,7,8,9,10,11,12]
avg_temp = [10, 12, 15, 20, 25, 28, 30, 28, 25, 20, 15, 12]

# Create a figure
fig = plt.figure()

#Create axes within the figure
ax = fig.add_subplot(1, 1, 1)

# Show the plot
plt.show()

#Bar chart 
plt.bar(months, avg_temp)
plt.show()

# Customizing your plots
ax.plot(months, avg_temp, color='red', linewidth=2, marker='o', markersize=8)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Average Monthly Temperature for 2021')

plt.show()
