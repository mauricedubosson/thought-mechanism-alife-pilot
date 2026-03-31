import matplotlib.pyplot as plt
import numpy as np

# Données extraites de ta simulation V20 (31 points, frame 0 à 2999)
frames = np.arange(0, 3100, 100)  # 31 points

stability = np.array([0.813, 0.328, 0.523, 0.347, 0.295, 0.476, 0.502, 0.559, 0.563, 0.539, 
                      0.329, 0.290, 0.365, 0.365, 0.479, 0.500, 0.544, 0.492, 0.654, 0.315, 
                      0.568, 0.303, 0.322, 0.571, 0.416, 0.603, 0.371, 0.372, 0.509, 0.593, 0.428])

population = np.array([87, 201, 98, 102, 103, 101, 102, 102, 103, 107, 100, 107, 108, 102, 104, 
                       102, 102, 101, 106, 105, 107, 100, 104, 103, 105, 107, 106, 98, 101, 102, 99])

multicellular = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

genome_mean = np.array([4.07, 5.05, 6.17, 6.40, 5.95, 5.62, 6.16, 6.15, 6.06, 5.76, 6.55, 6.70, 
                        6.43, 6.27, 6.20, 6.21, 6.37, 6.25, 6.43, 6.27, 6.50, 6.61, 6.37, 6.17, 
                        6.35, 6.36, 6.34, 6.27, 6.34, 6.51, 6.42])

nutrients = np.array([656, 16, 28, 14, 19, 8, 28, 23, 22, 8, 11, 6, 14, 17, 30, 29, 28, 27, 3, 11, 
                      6, 8, 12, 6, 19, 14, 12, 30, 25, 22, 17])

# Création des graphiques
fig, axs = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle('V20 Alife Pilot — Key Results (Dubosson Theory)', fontsize=16)

axs[0,0].plot(frames, stability, color='green', linewidth=2)
axs[0,0].set_title('Average Stability over Time')
axs[0,0].set_ylabel('Stability')
axs[0,0].grid(True, alpha=0.3)

axs[0,1].plot(frames, population, color='blue', linewidth=2)
axs[0,1].set_title('Population Size over Time')
axs[0,1].set_ylabel('Number of Vesicles')
axs[0,1].grid(True, alpha=0.3)

axs[1,0].plot(frames, multicellular, color='purple', linewidth=2)
axs[1,0].set_title('Multicellular Count over Time')
axs[1,0].set_ylabel('Number of Multicellular Organisms')
axs[1,0].grid(True, alpha=0.3)

axs[1,1].plot(frames, genome_mean, label='Mean Genome', color='orange', linewidth=2)
axs[1,1].plot(frames, np.full_like(frames, 8), label='Best Genome', color='red', linestyle='--', linewidth=2)
axs[1,1].set_title('Genome Evolution')
axs[1,1].set_ylabel('Genome Quality')
axs[1,1].legend()
axs[1,1].grid(True, alpha=0.3)

axs[2,0].plot(frames, nutrients, color='brown', linewidth=2)
axs[2,0].set_title('Nutrients Level over Time')
axs[2,0].set_ylabel('Nutrients')
axs[2,0].grid(True, alpha=0.3)

axs[2,1].axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('graphs/summary_v20.png', dpi=200, bbox_inches='tight')
plt.show()

print("✅ Graphiques générés avec succès dans le dossier 'graphs/'")
