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

  Let $f(X) = \left\| \widetilde{Y} - \widetilde{X} \right\|^2$, $g(X) = c^TX - b$,<br> the demensioin of $X$ and $Y$ is $N$,<br> and point $X^*$ is the **extreme point** satisfy all constraints, then

  $$\nabla L(X^*, \mu) = \nabla f(X^*) + \mu \nabla g(X^*) = 0$$
  $$\mu \geq 0, \quad \mu g(X^*)=0$$
