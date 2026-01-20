# The Two-dimensional Ising Model
## Introduction
The two-dimensional Ising model simulates the spin of atoms on a two-dimensional lattice.
The spin of an atom is affected by the spins of the other atoms on the lattice.
An atom flips its direction of spin according to how such a flip changes the Hamiltonian of the lattice.
The Hamiltonian $H$ of an $L \times L$ lattice is shown in the following equation, where $J$ is the interaction strength and $<i, j>$ denotes that $i$ is the neighbor of $j$.
$$ H = -J \sum_{<i, j>} s_i s_j $$

The Ising model simplifies the spin of atoms to either upward (1) or downward (-1).
## Implementation
I implements the Ising model simulation by the Wolff algorithm.
