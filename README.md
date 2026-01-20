# The Two-dimensional Ising Model
## Introduction
The two-dimensional Ising model simulates the spin of atoms on a two-dimensional lattice.
The spin of an atom is affected by the spins of the other atoms on the lattice.
An atom flips its spin according to how such a flip changes the energy in the lattice.
The energy of the system is computed according to the Hamiltonian $H$ in the following equation, where $J$ is the interaction strength between atoms.

$$H = -J \sum_{i, j \text{on the lattice}} s_i s_j$$

The Ising model simplifies the spin of atoms to either upward (1) or downward (-1).
## Implementation
I implement the Ising model simulation using the Wolff algorithm.
