# The Two-dimensional Ising Model
## Introduction
The two-dimensional Ising model simulates the spin direction of atoms on a two-dimensional lattice.
The spin direction of an atom is affected by the spin direction of the other atoms on the lattice.
An atom flips its spin direction based on how such a flip changes the energy of the lattice.
<!---
The energy of a lattice $L$ is computed according to the Hamiltonian $H$ in the following equation, where the set $n(i)$ consists of the neighbors of a point $i$ on the lattice, the term $J_{i, j}$ is the interaction strength between atom $i$ and atom $j$, the term $s_i$ denotes the spin direction of atom $i$, the function $f(\cdot, \cdot)$ is the energy between two atoms, the term $\mu$ is the magnetic momentum, and $h_i$ is the magnetic field on atom $i$.
--->
The energy of a lattice $L$ is computed according to the Hamiltonian $H$ in the following equation, where the meaning of each term is listed in the table below the equation.

$$H = -\sum_{i \in L} \sum_{j \in n(i)} J_{i, j} f(s_i, s_j) - \mu \sum_{i \in L} h_i s_i$$

| The term | Its meaning |
| :---: | --- |
| $n(i)$ | A set consisting of the neighbor of atom $i$ in the lattice |
| $J_{i, j}$ | The interaction strength between atom $i$ and atom $j$ |
| $s_i$ | The spin direction of atom $i$ |
| $f(\cdot, \cdot)$ | The energy between two atoms |
| $\mu$ | The magnetic moment |
| $h_i$ | The magnetic field operating on atom $i$ |

The Ising model simplifies the terms in the Hamiltonian as follows.
* The neighbors of an atom are those adjacent to it.
* The interaction strength $J_{i, j}$ is the same across all pairs of atoms.
* The spin of an atom is either upward (1) or downward (-1).
* The function $f(s_i, s_j)$ is the product of $s_i$ and $s_j$.
* The magnetic field is zero.

Under these simplifications, the Hamiltonian of the Ising model becomes as follows.

$$H = -J\sum_{i \in L} \sum_{j \in n(i)} s_i s_j$$

## Implementation
I implement the Ising model simulation using the Wolff algorithm.
The Wolff algorithm updates the spins in a lattice over time.
In each time step, the Wolff algorithm runs the following procedure, where $T$ is the temperature and $k_\beta$ is the Boltzmann constant.
1. Construct a cluster $C$.
2. Select an atom randomly and put it into the cluster $C$.
3. Assign the atom in $C$ as $s$.
3. For each neighbor $s' \in n(s)$ that has the same spin direction as $s$, add $s'$ to $C$ with probability $1 - e^{-2 J / (k_\beta T)}$.
4. If there is an atom in $C$ that hasn't be assigned as $s$, assign it as $s$ and go back to step 4.
5. Flip the spin direction of all atoms in $C$.
