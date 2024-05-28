import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

points = [(135, 234), (152, 535), (453, 124)]
image_path = 'Egypt.png'
image = mpimg.imread(image_path)

# Create a new plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8))

# Display the image
ax1.imshow(image)

# Customize the plot
ax1.set_title('Egypt')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')

x, y = [i[0] for i in points], [i[1]for i in points]
colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

for i in range(len(x) - 1):
    ax1.plot(x[i:i+2], y[i:i+2], color=colors[i])
ax1.plot([x[-1], x[0]], [y[-1], y[0]], color=colors[len(x) - 1])
ax1.scatter(x, y, c=colors, cmap='viridis')

text = []
for i in range(len(x)):
    if i == 0:
        s = [f"Start point: {x[0]}", i]

    elif i != len(x) - 1:
        s = [f"from {x[0]} to {x[1]}", i]
    
    else:
        s = [f"from {x[0]} to the start point {x[1]}", i]
    text.append(s)

ax2.axis('off')
table = ax2.table(cellText=text, colLabels=['Start Point', 'Destination'], cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.tight_layout()
plt.show()