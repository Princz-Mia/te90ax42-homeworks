import numpy as np
import matplotlib.pyplot as plt

# 1. FELADAT
# Eredeti bázisvektorok
original_basis = np.array([[1, 0], [0, 1]])

# Új bázisvektorok
new_basis = np.array([[1.5, -0.5], [0.5, 1.2]])

# Transzformációs mátrix meghatározása
A = np.linalg.inv(original_basis) @ new_basis
print("Transzformációs mátrix A:")
print(A)

# Az új bázisban lévő vektor
v_prime = np.array([2, 3])

# Vektor koordinátái az eredeti bázisban
v_original = np.linalg.inv(A) @ v_prime
print("A vektor koordinátái az eredeti bázisban:")
print(v_original)

# Ábrázolás
plt.figure(figsize=(10, 10))

# Eredeti bázisvektorok ábrázolása
plt.quiver(0, 0, original_basis[0, 0], original_basis[1, 0], angles='xy', scale_units='xy', scale=1, color='blue', label='Eredeti bázis: e1')
plt.quiver(0, 0, original_basis[0, 1], original_basis[1, 1], angles='xy', scale_units='xy', scale=1, color='cyan', label='Eredeti bázis: e2')

# Új bázisvektorok ábrázolása
plt.quiver(0, 0, new_basis[0, 0], new_basis[1, 0], angles='xy', scale_units='xy', scale=1, color='red', label="Új bázis: e1'")
plt.quiver(0, 0, new_basis[0, 1], new_basis[1, 1], angles='xy', scale_units='xy', scale=1, color='orange', label="Új bázis: e2'")

# Vektor ábrázolása
plt.quiver(0, 0, v_original[0], v_original[1], angles='xy', scale_units='xy', scale=1, color='green', label="v az eredeti bázisban")

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title("Eredeti és transzformált bázis")
plt.show()

# 2. FELADAT
# Transzformációs mátrix
A = np.array([[-2, 0.7], [0.1, 2]])

# Rácsháló generálása
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
original_grid = np.vstack([X.flatten(), Y.flatten()])

# Torzult térkép generálása
transformed_grid = A @ original_grid

# Ábrázolás
plt.figure(figsize=(20, 10))

# Eredeti térkép
plt.subplot(1, 2, 1)
plt.plot(original_grid[0], original_grid[1], 'o', markersize=2, label='Eredeti térkép')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Eredeti térkép")
plt.xlim(-6, 6)
plt.ylim(-6, 6)

# Torzult térkép
plt.subplot(1, 2, 2)
plt.plot(transformed_grid[0], transformed_grid[1], 'o', markersize=2, label='Torzult térkép')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Torzult térkép")
plt.xlim(-12, 12)
plt.ylim(-12, 12)

plt.show()

# 2.2 Kincs helye a torzított világban
v_prime = np.array([6, -2.5])
plt.figure(figsize=(10, 10))
plt.plot(transformed_grid[0], transformed_grid[1], 'o', markersize=2, label='Torzult térkép')
plt.quiver(0, 0, v_prime[0], v_prime[1], angles='xy', scale_units='xy', scale=1, color='red', label='Kincs helye (torzított térkép)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Kincs helye a torzított térképen")
plt.xlim(-12, 12)
plt.ylim(-12, 12)
plt.show()

# 2.3 Kincs helyének visszafejtése
v_original = np.linalg.inv(A) @ v_prime
print("A kincs tényleges helye az eredeti térképen:")
print(v_original)

# Kincs helye az eredeti térképen
plt.figure(figsize=(10, 10))
plt.plot(original_grid[0], original_grid[1], 'o', markersize=2, label='Eredeti térkép')
plt.quiver(0, 0, v_original[0], v_original[1], angles='xy', scale_units='xy', scale=1, color='green', label='Kincs helye (eredeti térkép)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Kincs helye az eredeti térképen")
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.show()
