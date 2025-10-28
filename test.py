import numpy as np
import matplotlib.pyplot as plt

# points = np.array([
#     [53.367, 7.207],    # Emden
#     [53.551, 9.994],    # Hamburg
#     [54.907, 8.303],    # Sylt (Westerland)
#     [54.783, 9.433],    # Flensburg
#     [53.893, 11.463],   # Wismar
#     [53.925, 14.133],   # Usedom
#     [51.154, 14.988],   # Görlitz
#     [50.312, 11.915],   # Hof (Bayern)
#     [48.575, 13.455],   # Passau
#     [47.594, 7.620],    # Weil am Rhein
#     [49.006, 8.404],    # Karlsruhe
#     [49.315, 6.751],    # Saarlouis
#     [51.788, 6.138]     # Kleve
# ])


points = np.array([
    [53.4, 7.2],   # Emden
    [53.6, 10.0],  # Hamburg
    [54.9, 8.3],   # Sylt
    [54.8, 9.4],   # Flensburg
    [53.9, 11.5],  # Wismar
    [53.9, 14.1],  # Usedom
    [51.2, 15.0],  # Görlitz
    [50.3, 11.9],  # Hof (Bayern)
    [48.6, 13.5],  # Passau
    [48.2, 12.8],  # Burghausen
    [47.8, 13.0],  # Salzburg
    [47.5, 11.1],  # Garmisch-Partenkirchen
    [47.6, 7.6],   # Weil am Rhein
    [49.0, 8.4],   # Karlsruhe
    [49.3, 6.8],   # Saarlouis
    [51.8, 6.1]    # Kleve
])

points = points - np.array([47, 6])

print(points)

polygon = np.vstack([points, points[0]])

# Plot der gescalten Koordinaten
plt.figure(figsize=(6,6))
plt.plot(polygon[:, 1], polygon[:, 0], '-o', color='royalblue')
plt.show()
