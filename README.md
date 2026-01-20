# The Two-dimensional Ising Model
## Introduction
The two-dimensional Ising model simulates the spin of atoms on a two-dimensional lattice.
The spin of an atom is affected by the spins of the other atoms on the lattice.
An atom flips its spin direction according to how such a flip changes the energy of the lattice.
The energy of a lattice $L$ is computed according to the Hamiltonian $H$ in the following equation, where $J$ is the interaction strength between atoms, the term $s_i$ denotes the spin direction of an atom $i$, the set $n(i)$ consists of the neighbors of a point $i$ on the lattice, and $f(\cdot, \cdot)$ is the energy between two atoms.

$$H = -J \sum_{i \in L} \sum_{j \in n(i)} f(s_i, s_j)$$

The Ising model simplifies the terms in the Hamiltonian as follows.
* The spin of an atom is either upward (1) or downward (-1).
* The neighbors of an atom are those adjacent to it.
* The function $f(s_i, s_j)$ is the product of $s_i$ and $s_j$.

## Implementation
I implement the Ising model simulation using the Wolff algorithm.
The Wolff algorithm updates the spins in a lattice along time.
In each time step, the Wolff algortihm rums the following procedure, where $T$ is the temperature and $k_\beta$ is the Boltzmann constant.
1. Construct a cluster $C$.
2. Select an atom $s$ randomly and put it into the cluster $C$.
3. For each neighbor $s' \in n(s)$ that has the same spin direction as $s$, add $s'$ to $C$ with probability $1 - e^{-2 J / (k_\beta T)}$.
4. If there is an atom in $C$ that hasn't be selected as $s$, select it as $s$ and go back to step 3.
5. Flip the spin direction of all atoms that have been in $C$.
