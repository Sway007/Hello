## <font color="blue"> 1.1 </font>
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


## <font color="blue"> 1.2 </font>
$$E(W)=\frac{1}{2}\sum^N_{n=1}\{y(x_n,W)-t_n\} + \frac{\lambda}{2}||W||^2$$

derivatitive $E(W)$ with respect to $w_i$, wo obtain

$$\frac{\partial{E(W)}}{\partial{w_i}}=\sum_{n=1}^{N}\{\sum_{j=0}^Mw_jx_n^j-t_n\}x_n^i + \lambda w_i$$

set the derivative to 0 

$$\sum_{n=1}^N\sum_{j=0}^Mx_n^{i+j}w_j - \sum_{n=1}^Nx_n^it_n + \lambda w_i = 0$$

and with the  notation of **exercise 1.1**, we have

$$\sum_{j=0}^MA_{ij}w_j - T_i + \lambda w_i = 0$$

## <font color="blue"> 1.3 </font>

* <font size="4">Probability of selecting an apple </font>

    Denote the probability of selecting an apple with $P(A)$, and denote the probability of selecting from box `b, g, r` with respectively $P(A, b), P(A, g), P(A, r)$. 
    According to _**the law of total probability**_, we have

    $$P(A) = P(A, b) + P(A, g) + P(A, r) $$
    $$P(A) = P(A| b) * p(b) + P(A|g) * p(g) + P(A| r) * p(r)$$

    from the description of textbook we can infer easily that: $P(A|r)=3/10$, $P(A|b)=1/2$, $P(A|g)=3/10$. so:

    $$P(A) = \frac{3}{10} * 0.2 + \frac12 * 0.2+ \frac{3}{10} * 0.6 = 0.34$$

* <font size="4">Probability that select an orange from the green box</font>

    we denote the event that selecting an _**orange**_ with _**O**_,  then the probability we try to figure out can be represented as $P(g | O)$. according to _**Bayes Theorem**_, 

    $$P(g|O) =  \frac{P(g, O)}{P(O)} = \frac{P(O|g) P(g)}{P(O|r)P(r) + P(O|g)P(g) + P(O|b)P(b)}$$

    cause $P(O|r)=4/10$, $P(O|g) = 3/10$, $P(O|b) = 1/2$, so:

    $$P(g|O) = \frac{\frac{3}{10} * 0.6}{\frac{4}{10} * 0.2 + \frac{3}{10} * 0.6 + \frac12*0.2} = 0.5$$


## <font color="blue"> 1.6 </font>

First, I try to show that _**`the joint probability's Expectation of two independent variables equals to the multiplication of the two variable's Expectation`**_, namely:


$$E(XY) = E(X)E(Y)\qquad if X\ and\ Y\ is\ dependent \qquad (1) $$

Proof:

$$E(XY) = \int xyf(xy)dxdy$$
$$E(XY)=\int xyf(x)f(y)dxdy$$
$$E(XY)=\int xf(x)dx\ *\ \int yf(y)dy = E(X) * E(Y) $$

then the covariance of X and Y:

$$COV(X, Y) = E(\ (X - EX)(Y-EY)\ )$$
$$COV(X, Y) = E(XY) - E(X)E(Y)$$

according to **(1)**, we get

$$COV(X, Y) = 0$$


## <font color="blue"> 1.10 </font>

* Expectaion:

    $$E(X+Y) = \int(x+y)f(x, y)dxdy$$
    $$E(X+Y) = \int x\int f(x,y)dydx\ +\ \int y\int f(x,y)dxdy $$
    $$E(X+Y) = \int xf_{X}(x)dx + \int yf_{Y}(y)dy$$
    $$E(X+Y) = E(X) + E(Y)$$

* Variance:

    $$var(X + Y) = E(X+Y)^2 - (E(X+Y))^2$$
    $$var(X + Y) = E(X^2 + Y^2 + 2XY) - (EX + EY)^2$$
    $$var(X + Y) = EX^2 + EY^2 + 2EXY - (EX)^2 - (EY)^2 - 2EXEY$$

    cause X and Y is dependent, so $EXY=EX\;EY$, then we get:

    $$var(X + Y) = EX^2 - (EX)^2 + EY^2 - (EY)^2$$
    $$var(X + Y) = var(X) + var(Y)$$

## <font color="blue"> 1.17 </font>

* $\Gamma(n + 1) = n\Gamma(n) \qquad (1)$

    $$\Gamma(n + 1) = \int_0^{\infty}x^{n}e^{-x}dx = -\int_0^{\infty} x^{n}de^{-x}$$
    $$\Gamma(n + 1) = -x^ne^{-x}|^{\infty}_0 + n\int_0^{\infty}x^{n-1}e^{-x}dx = n\int_0^{\infty}x^{n-1}e^{-x}dx$$
    $$\Gamma(n+1)=n\Gamma(n)$$

* $\Gamma(1) = 1$

    $$\Gamma(1) = \int_0^{\infty}x^0e^{-x}dx = \int_0^{\infty}e^{-x}dx = e^0 - e^{-\infty} = 1$$

* $\Gamma(x+1) =  x! \qquad if\ x\ is\ an\ integer \qquad (2)$

    according to (1) and (2)

    $$\Gamma(x+1) = x!\Gamma(1) = x!$$

## <font color="blue"> 1.25 </font>

The expected loss function of multiple target variables:

$$E(L(t, y(x))) = \int \int ||y(x) - t||^2p(x, t)dxdt$$

to obtain a $\tilde{y}$ which minimize the $E(L)$, we derivative $E$ partially with repect to $y(x)$:

$$\frac {\partial E(t, y(x))} {\partial{y(x)}} = 
2\int \int y(x)p(x,t) - tp(t, x)dxdt = \int y(x)p(x) - (\int tp(t, ,x)dx)\ dt$$

set the partial derivative to 0, then

$$y(x)=\frac {\int tp(t,x)dt}{p(x)} = \int tp(t|x)dt = E(t|x)$$

## <font color="blue"> 1.30 </font>

$$KL(p||q)=-\int p(x)ln(\frac{q(x)}{q(x)})dx$$

substitute $p(x)=N(x|\mu, \sigma^2),\ q(x)=N(x|m, s^2)$, hence

$$KL(p||q)=-\int \frac{ln\frac{\sigma}s}{\sqrt{2\pi}\sigma}EXP(-\frac{(x-\mu)^2}{2\sigma^2}) + \frac{(x-\mu)^2}{2\sigma^2} - \frac{(x-m)^2}{2s^2}dx$$

## <font color="blue"> 1.40 </font>

Let $f(x)=lnx$, cause $\frac{df^2}{(dx)^2}=-\frac1{x^2}\leq0$, so $f(x)$ is a concave function, hence

$$f(\frac{\sum_{i=1}^{N}x_i}{N}) \geq \frac{\sum_{i=1}^{N}f(x_i)}N{}$$
$$ln(\frac{\sum_{i=1}^{N}x_i}{N}) \geq \frac 1Nln(\prod _{i=1}^N x_i)=ln\sqrt [N]{\prod_{i=1}^{N}x_i}$$

obviously $f(x)=ln(x)$ is Monotonic, so we have

$$\frac{\sum_{i=1}^{N}x_i}{N} \geq \sqrt [N]{\prod_{i=1}^{N}x_i}$$

namely, 

>_the arithmetic mean of a set of real numbers is never less than their grometrical mean_

## <font color="blue"> 1.41 </font>

$$I(x,y) = -\int \int p(x, y) ln(\frac{ p(x)p(y) }{ p(x, y) })dxdy$$
$$I(x,y) =\int \int p(x, y)ln\frac {p(x,y)}{p(y)}dxdy -\int \int p(x, y)ln\ p(x) dxdy$$
$$I(x,y) = \int \int p(x,y)ln\ p(x|y)dxdy - \int p(x)ln p(x)dx$$
$$I(x,y) = -H(x|y) + H(x)$$

the same rules apply for $I(x, y) = H(y) - H(y|x)$
