Кононыхин Егор мф-71
#задача 3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource

# Создаем координаты X, Y
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X_grid, Y_grid = np.meshgrid(X, Y)

# Функция рельефа (горы и холмы)
Z_grid = np.sin(np.sqrt(X_grid**2 + Y_grid**2)) * 2 + np.cos(Y_grid) * 1.5

# Добавляем источник света
ls = LightSource(azdeg=315, altdeg=45)

# Используем plt.cm.terrain вместо 'terrain'
shaded_Z = ls.shade(Z_grid, cmap=plt.cm.terrain, vert_exag=0.2, blend_mode='soft')

# Создаем 3D-график
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Отображаем рельеф с тенью
ax.plot_surface(X_grid, Y_grid, Z_grid, facecolors=shaded_Z, rstride=1, cstride=1)

# Настройки осей
ax.set_xlabel("X координата")
ax.set_ylabel("Y координата")
ax.set_zlabel("Высота (Z)")

plt.show()

#Задача 2
import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_excel('data.xlsx')
x = table.values[:, 0]
y = table.values[:, 1]
plt.figure(figsize=(15, 7))
plt.plot(x, y)
plt.show()
#задача 1

import pandas as pd
num1=int(input("напиши номер строки"))
print(df.iloc[num1])
