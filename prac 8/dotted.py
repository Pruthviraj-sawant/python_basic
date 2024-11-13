# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Create some data for the graph
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)  # Sine of the x values

# Create the plot with a dotted line (using linestyle ':')
plt.plot(x, y, linestyle=':', color='b', label='Sine Wave')  # Blue dotted line

# Adding titles and labels
plt.title('Dotted Line Graph: Sine Wave')
plt.xlabel('X-Axis (radians)')
plt.ylabel('Y-Axis (sin(x))')

# Show the legend to identify the plot
plt.legend()

# Show the plot
plt.show()
