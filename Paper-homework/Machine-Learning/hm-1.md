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
