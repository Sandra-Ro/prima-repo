import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series([6, 14, 8, 18, 4], index=['Horses', 'Cows', 'Goats', 'Sheep', 'Cattle'], )
colors = ['green','yellow','violet','blue', 'black']
s.plot(kind='bar', color=colors)
plt.title('Domestic animals', fontsize=20, fontname='Comic Sans MS')
plt.text(0, 6, '6')
plt.text(1, 14,'14')
plt.text(2, 8,'8')
plt.text(3, 18,'18')
plt.text(4, 4,'4')
plt.grid(True, color='red')
plt.show()
