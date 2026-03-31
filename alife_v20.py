import numpy as np
import random

# ======================== V20 ALIFE PILOT - SÉNESCENCE INTELLIGENTE + SYMBIOSE ========================
MAX_VESICLES = 300
FRAMES = 3000
INITIAL_NUTRIENTS = 680.0
NUTRIENT_REPLENISH = 2.6

NUM_VESICLES = 80
WORLD_SIZE = 1000
BASE_GOOD_PROB = 0.6
STABILITY_DECAY = 0.958
ASSOCIATION_DISTANCE = 80
ASSOCIATION_THRESHOLD = 0.88
MUTATION_RATE = 0.19
RECOMBINATION_RATE = 0.45

GENOME_LENGTH = 8

class Vesicle:
    def __init__(self, x, y, is_multicellular=False, genome=None, age=0):
        self.x = x
        self.y = y
        self.radius = 35.0
        self.stability = 0.85
        self.channel_memory = {}
        self.cluster_id = None
        self.is_multicellular = is_multicellular
        self.genome = genome if genome is not None else [random.randint(0,1) for _ in range(GENOME_LENGTH)]
        self.age = age
        self.metabolic_efficiency = sum(self.genome) / GENOME_LENGTH

    def genome_quality(self):
        return sum(self.genome) / GENOME_LENGTH

    def max_age(self, population_density):
        # Sénescence intelligente : plus la population est dense, plus la sénescence est précoce
        base = 140
        density_penalty = int(40 * population_density)
        quality_bonus = int(60 * self.genome_quality())
        return max(60, base - density_penalty + quality_bonus)

    def receive_molecule(self, is_good):
        if is_good:
            self.stability = min(1.0, self.stability + 0.20 * self.metabolic_efficiency)
        else:
            self.stability = max(0.0, self.stability - 0.38)
            self.channel_memory["bad"] = min(1.0, self.channel_memory.get("bad", 0) + 0.42)

    def anticipate(self):
        return "bad" in self.channel_memory and self.channel_memory["bad"] > 0.78 and random.random() < self.channel_memory["bad"]

    def replicate_genome(self):
        new_genome = self.genome.copy()
        for i in range(len(new_genome)):
            if random.random() < MUTATION_RATE:
                new_genome[i] = 1 - new_genome[i]
        return new_genome

    def recombine_with(self, other):
        if random.random() < RECOMBINATION_RATE:
            cut = random.randint(1, GENOME_LENGTH-1)
            self.genome = self.genome[:cut] + other.genome[cut:]
            other.genome = other.genome[:cut] + self.genome[cut:]

    def update(self, nutrients, population_density):
        self.age += 1
        cost = 8.5 if self.is_multicellular else 4.2
        if nutrients < cost:
            self.stability *= 0.45
        else:
            self.stability = min(1.0, self.stability + 0.055 * self.metabolic_efficiency)
        self.stability *= STABILITY_DECAY

        # Sénescence intelligente
        if self.age > self.max_age(population_density):
            self.stability *= 0.32
        return self.stability > 0.05

# ======================== INITIALISATION ========================
vesicles = [Vesicle(random.uniform(100, WORLD_SIZE-100), random.uniform(100, WORLD_SIZE-100)) 
            for _ in range(NUM_VESICLES)]
nutrients = INITIAL_NUTRIENTS
current_good_prob = BASE_GOOD_PROB

print("🚀 Simulation V20 (théorie Dubosson) - Sénescence intelligente + symbiose en cours...\n")

for frame in range(FRAMES):
    if frame % 80 == 0:
        current_good_prob = BASE_GOOD_PROB + random.uniform(-0.55, 0.55)
        current_good_prob = max(0.18, min(0.98, current_good_prob))

    population_density = len(vesicles) / MAX_VESICLES

    alive = []
    for v in vesicles:
        if v.update(nutrients, population_density):
            alive.append(v)

    # Association + recombinaison + symbiose
    for i in range(len(alive)):
        for j in range(i+1, len(alive)):
            if alive[i].cluster_id is None and alive[j].cluster_id is None:
                dx = alive[i].x - alive[j].x
                dy = alive[i].y - alive[j].y
                if dx*dx + dy*dy < ASSOCIATION_DISTANCE**2:
                    if alive[i].stability > ASSOCIATION_THRESHOLD and alive[j].stability > ASSOCIATION_THRESHOLD:
                        cluster_id = frame
                        alive[i].cluster_id = alive[j].cluster_id = cluster_id
                        alive[i].is_multicellular = alive[j].is_multicellular = True
                        # Partage mémoire
                        for mol, strength in list(alive[i].channel_memory.items()):
                            alive[j].channel_memory[mol] = max(alive[j].channel_memory.get(mol, 0), strength)
                        for mol, strength in list(alive[j].channel_memory.items()):
                            alive[i].channel_memory[mol] = max(alive[i].channel_memory.get(mol, 0), strength)
                        # Recombinaison + symbiose
                        alive[i].recombine_with(alive[j])

    # Reproduction
    new_vesicles = []
    for v in alive:
        prob = 0.17 if v.is_multicellular else 0.045
        prob += 0.10 * v.genome_quality()
        cost = 9.0 if v.is_multicellular else 4.5
        if v.stability > 0.68 and random.random() < prob and nutrients > cost and len(alive) + len(new_vesicles) < MAX_VESICLES:
            nutrients -= cost
            new_genome = v.replicate_genome()
            new_v = Vesicle(v.x + random.uniform(-40, 40), v.y + random.uniform(-40, 40), v.is_multicellular, new_genome)
            new_v.stability = v.stability * 0.52
            new_v.channel_memory = v.channel_memory.copy()
            new_vesicles.append(new_v)

    vesicles = alive + new_vesicles
    nutrients = min(INITIAL_NUTRIENTS, nutrients + NUTRIENT_REPLENISH)

    if frame % 100 == 0 or frame == FRAMES-1:
        multicell = sum(1 for v in vesicles if v.is_multicellular)
        avg_genome = np.mean([sum(v.genome) for v in vesicles])
        best_genome = max([sum(v.genome) for v in vesicles])
        senescence_deaths = sum(1 for v in vesicles if v.age > v.max_age(population_density))
        print(f"Frame {frame:4d} → Vésicules : {len(vesicles):3d} | Multicellulaires : {multicell:3d} | "
              f"Stabilité : {np.mean([v.stability for v in vesicles]):.3f} | "
              f"Génome moyen : {avg_genome:.2f}/{GENOME_LENGTH} | Meilleur : {best_genome} | "
              f"Nutriments : {nutrients:.0f} | Sénescence : {senescence_deaths}")

print("\n✅ Simulation V20 terminée avec succès !")
print(f"Population finale : {len(vesicles)} vésicules")
print(f"Multicellulaires   : {sum(1 for v in vesicles if v.is_multicellular)}")
print(f"Stabilité moyenne  : {np.mean([v.stability for v in vesicles]):.3f}")
print(f"Génome moyen       : {np.mean([sum(v.genome) for v in vesicles]):.2f}/{GENOME_LENGTH}")
print(f"Meilleur génome    : {max([sum(v.genome) for v in vesicles])}/{GENOME_LENGTH}")
