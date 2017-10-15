* Projection of 𝑧 onto set 𝑆, denoted often 𝑃(𝑧; 𝑆) amounts to finding the closest point (in the Euclidean metric) in 𝑆 from 𝑥
* Assume that 𝑆 = 𝑥 𝑐 ⊤𝑥 ≤ 𝑏+ for some vector 𝑐 and some scalar 𝑏
*  Write this as a optimization problem, determine which kind of problem it is
(linear, quadratic, …)

* Provide a close-form formula to find the projection for arbitrary 𝑐, 𝑏 and �


## _**Optimization Problem**_

* assume sets: $Z=\{Y | z(y)=0\}, \quad S=\{X| c^Tx \leq b\}$
* projection $P\lgroup\ Z(y)\to S(x)\ \rgroup$:

  for any $\widetilde{Y} \in Z$, find $\widetilde{X} \in S$, such that $min\left\| \widetilde{Y} - \widetilde{X} \right\|^2$.

all above can be represented as:

$\quad \widetilde Y \in Z: z(\widetilde Y)=0,\quad min\left\| \widetilde{Y} - \widetilde{X} \right\|^2$

$s.t. :$

$\quad c^TX \leq b$

  it can be infered from the formula that this problem is _**Quadratic**_

* close-form formula:

TODO
