## 1.1
<font size=4>Proof:</font>

 Let:
 
 $$y(x, w)=w_{0}+w_1x+w_2x^2+...+w_Mx^M = \sum_{j=0}^Mw_jx^j$$

 Error function:

 $$E(w)=\frac{1}{2}\sum_{n=1}^{N}\{{y(x_n,w)-t_n}\}^2=\frac{1}{2}\sum_{n=1}^{N}\{\sum_{j=0}^{M}w_jx^j_{n}-t_n\}^2$$

 so we have:

 $$\frac{\partial{E(w)}}{\partial{w_i}}=\sum_{n=1}^{N}\{\sum_{j=0}^Mw_jx_n^j-t_n\}x_n^i$$

 let the partial derivative be zero, we get:

 $$\sum_{n=1}^N\sum_{j=0}^{M}w_jx_n^{i+j}=\sum_{n=1}^Nt_nx_n^i$$

 Let $A_{ij}=\sum_{n=0}^Mx_n^{i+j}$ , $T_i=\sum_{n=1}^Nt_nx_n^i$ . eventually, we got
 
 $$\sum_{j=0}^MA_{ij}w_j=T_i$$


## 1.2
$$E(W)=\frac{1}{2}\sum^N_{n=1}\{y(x_n,W)-t_n\} + \frac{\lambda}{2}||W||^2$$

derivatitive $E(W)$ with respect to $w_i$, wo obtain

$$\frac{\partial{E(W)}}{\partial{w_i}}=\sum_{n=1}^{N}\{\sum_{j=0}^Mw_jx_n^j-t_n\}x_n^i + \lambda w_i$$

set the derivative to 0 

$$\sum_{n=1}^N\sum_{j=0}^Mx_n^{i+j}w_j - \sum_{n=1}^Nx_n^it_n + \lambda w_i = 0$$

and with the  notation of **exercise 1.1**, we have

$$\sum_{j=0}^MA_{ij}w_j - T_i + \lambda w_i = 0$$

## 1.3

* <font size="4">Probability of selecting an apple </font>

    Denote the probability of selecting an apple with $P(A)$, and denote the probability of selecting from box `b, g, r` with respectively $P(A, b), P(A, g), P(A, r)$. 
    According to _**the law of total probability**_, we have

    $$P(A) = P(A, b) + P(A, g) + P(A, r)$$
    $$P(A) = P(A| b) * p(b) + P(A|g) * p(g) + P(A| r) * p(r)$$

    from the description of textbook we can infer easily that: $P(A|r)=3/10$, $P(A|b)=1/2$, $P(A|g)=3/10$. so:

    $$P(A) = \frac{3}{10} * 0.2 + \frac12 * 0.2+ \frac{3}{10} * 0.6 = 0.34$$

* <font size="4">Probability that select an orange from the green box</font>

    we denote the event that selecting an _**orange**_ with _**O**_,  then the probability we try to figure out can be represented as $P(g | O)$. according to _**Bayes Theorem**_, 

    $$P(g|O) =  \frac{P(g, O)}{P(O)} = \frac{P(O|g) P(g)}{P(O|r)P(r) + P(O|g)P(g) + P(O|b)P(b)}$$

    cause $P(O|r)=4/10$, $P(O|g) = 3/10$, $P(O|b) = 1/2$, so:

    $$P(g|O) = \frac{\frac{3}{10} * 0.6}{\frac{4}{10} * 0.2 + \frac{3}{10} * 0.6 + \frac12*0.2} = 0.5$$


## TODO
