# The Two-dimensional Ising Model
## Introduction
The two-dimensional Ising model simulates the spin of atoms on a two-dimensional lattice.
The spin of an atom is affected by the spins of the other atoms on the lattice.
An atom flips its spin direction according to how such a flip changes the energy of the lattice.
The energy of a lattice $L$ is computed according to the Hamiltonian $H$ in the following equation, where $J$ is the interaction strength between atoms, $s_i$ is the spin direction of an atom $i$, $n(i)$ is the neighbors of a point $i$ on the lattice, and $f(\cdot, \cdot)$ is the energy of two atoms.

$$H = -J \sum_{i \in L} \sum_{j \in n(i)} f(s_i, s_j)$$

The Ising model simplifies the terms in the Hamiltonian as follows.
* The spin of an atom is either upward (1) or downward (-1).
* The neighbors of an atom are those adjacent to it.
* The function $f(s_i, s_j)$ is the product of $s_i$ and $s_j$.

## Implementation
I implement the Ising model simulation using the Wolff algorithm.
