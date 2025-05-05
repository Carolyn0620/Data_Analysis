import matplotlib.pyplot as plt
import seaborn as sns

# Your data
data = [89, 47, 164, 296, 30, 215, 138, 78, 48, 39]

# Create the horizontal box plot
plt.figure(figsize=(5, 2))
sns.boxplot(data=data, orient="h")

# Add labels
plt.title("Horizontal Box Plot of Given Data")
plt.ylabel("Values")

# Show the plot
plt.show()