# thought-mechanism-alife-pilot
markdown

# Artificial Life Pilot — Testing Dubosson’s Theory of Primitive Thought

**Author**: Maurice Dubosson  
**Computational collaboration**: Grok (xAI)  
**Version**: V20 (final pilot)  
**Date**: March 2026

## Goal of the Project

This repository contains a series of computational experiments (V1 to V20) designed to explore the core ideas presented in the essay *"How to Find a Model of the Mechanism of Thought"*.

The central hypothesis is that **primitive thought** ("good for me / bad for me") emerges at the level of the protocell membrane and drives autopoiesis, self-organisation, anticipation, and the long-term continuation of life. When ecological niches become too narrow, the system may "invent" programmed death (senescence) to maintain dynamic continuation instead of freezing in a stable equilibrium.

## Important Disclaimer

**These are computational toy models, not empirical scientific proofs.**

All simulations are highly simplified (short genome, minimal physics, abstract chemistry). They do **not** constitute experimental evidence for the origin of life, the emergence of thought, or biological evolution.  

They are exploratory tools intended to:
- Illustrate the logical consequences of the proposed mechanism
- Test whether the internal "good/bad" judgment + autopoiesis can sustain open-ended dynamics
- Highlight strengths and limitations of the theory

We strongly encourage researchers in biology, complex systems, artificial life, philosophy of biology, and cognitive science to **criticise, improve, extend, or compare** this work with existing models (autopoiesis, artificial chemistry, Tierra, Avida, evolutionary game theory, etc.).

## Summary of the Pilot (V1 → V20)

We iteratively built a minimal Artificial Life model based on:
- Protocell membrane as the first "brain"
- Primitive judgment "good for me / bad for me"
- Anticipation via adaptive ion channels
- Autopoiesis (self-maintenance)
- Transition to multicellularity with memory sharing
- Primitive genome
- Metabolism and resource competition
- Senescence (programmed death) modulated by genome quality and population density

**Key observations**:
- Pure Darwinian selection + mutation quickly leads to stable plateaus.
- Adding the internal "good/bad" mechanism creates strong self-organisation and resilience.
- When niches become too narrow, **senescence** prevents freezing and restores dynamic turnover.
- The most dynamic behaviour appears in later versions with modulated senescence, catastrophes, and strong competition.

The model suggests that **Darwinian selection alone is not sufficient** to maintain open-ended evolution in simple landscapes. An internal auto-organising force (primitive thought + autopoiesis + senescence) appears necessary for continued dynamism.

## Repository Contents

- `alife_v20.py` → The final V20 simulation code
- `HOW_TO_FIND_A_MODEL_OF_THE_MECHANISM_OF_THOUGHT.md` → Full original theory text
- `README.md` → This file

## How to Run

```bash
pip install numpy
python alife_v20.py

markdown

## Key Results from V20 Simulation

![V20 Alife Pilot — Key Results (Dubosson Theory)](graphs/summary_v20.png)

*Note: These are computational toy models, not empirical evidence. They illustrate the logical consequences o
markdown

## Comparison with Existing Artificial Life Models

This pilot is deliberately minimal and grounded in Dubosson’s philosophical and theoretical framework. Below is a brief comparison with some well-known Artificial Life systems:

| Model                  | Year     | Core Mechanism                          | Key Focus                          | Similarity with Dubosson Pilot                  | Main Difference |
|------------------------|----------|-----------------------------------------|------------------------------------|--------------------------------------------------|-----------------|
| **Tierra** (Tom Ray)   | 1991     | Self-replicating machine code in memory | Open-ended evolution               | Digital organisms competing for resources        | No embodiment, no primitive thought, no explicit senescence |
| **Avida** (Ofria et al.) | 1993–   | Digital genomes with explicit fitness   | Evolutionary dynamics              | Genome, mutation, selection                    | Highly engineered fitness functions; no membrane-level cognition |
| **PolyWorld** (Yaeger) | 1994     | Embodied agents with neural networks    | Ecology + neural evolution         | Embodied agents, resource competition          | Complex neural networks instead of membrane-based primitive thought |
| **Autopoiesis models** (Maturana/Varela, Bourgine & Stewart) | 1970s–   | Self-maintaining networks               | Autopoiesis & cognition            | Strong focus on self-maintenance and unity     | Mostly theoretical; our pilot adds explicit “good/bad” judgment and senescence |
| **Artificial Chemistry** (Fontana, Dittrich, etc.) | 1990s–   | Reactive molecules in a soup            | Chemical self-organisation         | Chemistry-like rules                           | No explicit membrane or primitive thought |

### What makes the Dubosson Pilot distinctive

- **Primitive thought at the membrane level**: The “good for me / bad for me” judgment is not an add-on but the fundamental mechanism of the system.
- **Senescence as an evolved trait**: Death is not just a side-effect of resource limits but can be “invented” by the system itself to maintain long-term continuation when niches become too narrow.
- **Autopoiesis + internal cognition**: The model tries to combine self-maintenance with a minimal form of anticipation and decision-making from the very first protocell.

These simulations are **not empirical proofs** but computational explorations. They suggest that an internal organising principle (primitive thought + autopoiesis + regulated senescence) may be necessary to sustain open-ended dynamics beyond what pure Darwinian selection achieves in simple landscapes.

We invite researchers to critique these assumptions, extend the model, or compare it more rigorously with existing frameworks.



 

