# A bounded update reveals hidden orientation

The exponential update and the measurement update have different responses when the prior and the evidence do not commute. This page computes a response difference that stays finite as the Hilbert-space dimension grows. The [copy lower bound](copy_lower_bound.md) turns that difference into a resource obstruction.

Throughout, logarithms are natural. For a positive definite density operator $\rho$ and a Hermitian evidence operator $H$, write

$$
\mathcal E_H(\rho)
=\frac{\exp(\log\rho+H)}{\operatorname{Tr}\exp(\log\rho+H)}.
$$

No oracle for $\log\rho$ is assumed. This expression defines the desired output state.

## The family and the observable

Let $D\ge 2$ be even and fix

$$
Z=\operatorname{diag}(\underbrace{1,\ldots,1}_{D/2},
\underbrace{-1,\ldots,-1}_{D/2}).
$$

For $0<a<1$ and a unitary $U$, define

$$
\rho_0=\frac{I}{D},\qquad
\rho_U=\frac{I+aUZU^\dagger}{D}.
$$

The eigenvalues of every $\rho_U$ are $(1+a)/D$ and $(1-a)/D$, each with multiplicity $D/2$. The eigenvalue ratio is the fixed number $(1+a)/(1-a)$. The comparison with $\rho_0$ first proves a two-spectrum intermediate result. The main [copy lower bound](copy_lower_bound.md) replaces $\rho_0$ by a commuting ensemble with exactly the same spectrum as $\rho_U$; its actual input spectrum may therefore be supplied to the algorithm.

The evidence is the known operator $H=hZ$. Its norm is $h$, independent of $D$. The statistic of interest is one fixed output observable:

$$
m_U(t)=\operatorname{Tr}\!\left[Z\mathcal E_{tZ}(\rho_U)\right].
$$

For the maximally mixed prior, the answer is explicit:

$$
m_0(t)=\tanh t.
$$

We use Haar-random $U$ only as a lower-bound distribution. An update algorithm is required to work for every promised input and is not supplied with $U$.

## Uniform control of the finite update

**Lemma 1 (partition-function derivatives).** Let $A$ and $Z$ be finite-dimensional Hermitian matrices with $\|Z\|\le1$, and put

$$
F(t)=\operatorname{Tr}e^{A+tZ},\qquad m(t)=\frac{F'(t)}{F(t)}.
$$

For every real $t$ and every integer $k\ge1$,

$$
|F^{(k)}(t)|\le F(t).
$$

In particular,

$$
|m''(t)|\le6,\qquad |m'''(t)|\le26.
$$

**Proof.** Write $K=A+tZ$. Iterating the Duhamel formula gives

$$
F^{(k)}(t)=k!\int_{\Delta_k}
\operatorname{Tr}\!\left(e^{s_0K}Z e^{s_1K}Z\cdots Z e^{s_kK}\right)ds,
$$

where $\Delta_k=\{(s_0,\ldots,s_k):s_j\ge0,\sum_js_j=1\}$ has volume $1/k!$ in the usual $k$ independent coordinates. Schatten Holder bounds every integrand in magnitude by

$$
\prod_{j=0}^k\|e^{s_jK}\|_{1/s_j}\,\|Z\|^k
\le\prod_{j=0}^k(\operatorname{Tr}e^K)^{s_j}
=F(t).
$$

When $s_j=0$, the corresponding factor is interpreted in the operator norm. Integrating proves the derivative bound. Since $m=(\log F)'$,

$$
m''=\frac{F'''}F-3\frac{F''F'}{F^2}
+2\frac{(F')^3}{F^3},
$$

and

$$
m'''=\frac{F''''}F-4\frac{F'''F'}{F^2}
-3\left(\frac{F''}F\right)^2
+12\frac{F''(F')^2}{F^3}
-6\frac{(F')^4}{F^4}.
$$

Taking absolute values gives $1+3+2=6$ and $1+4+3+12+6=26$. These estimates depend on neither the dimension nor the spectrum of $A$. $\square$

## The exact susceptibility

Let $\overline m(t)=\mathbb E_U m_U(t)$, with normalized Haar measure. Define

$$
c(a)=\frac12+\frac{a}{\log((1+a)/(1-a))}.
$$

Because $\operatorname{atanh}a>a$ for $0<a<1$, one has $1/2<c(a)<1$.

**Lemma 2 (finite-dimensional Haar response).** For every even $D\ge2$,

$$
\overline m(0)=0,\qquad
\overline m'(0)=c_D(a)
=\frac{D^2c(a)-1-a^2}{D^2-1}
\le c(a).
$$

Moreover, $\overline m(t)$ is an odd function of $t$.

**Proof.** If $\rho$ has eigenvalues $p_i>0$, Duhamel differentiation of $\operatorname{Tr}e^{\log\rho+tZ}$ gives

$$
m'(0)=\int_0^1\operatorname{Tr}(\rho^{1-s}Z\rho^sZ)\,ds
-(\operatorname{Tr}\rho Z)^2.
$$

In an eigenbasis of $\rho$, this becomes

$$
m'(0)=\sum_{i,j}L(p_i,p_j)|W_{ij}|^2-\mu^2,
\qquad \mu=\sum_i p_iW_{ii},
$$

where $W$ is $Z$ in that basis and

$$
L(x,y)=\frac{x-y}{\log x-\log y},\qquad L(x,x)=x
$$

is the logarithmic mean. For our family, $W=U^\dagger ZU$ is a Haar conjugate of a traceless Hermitian involution. Its second moment is

$$
\mathbb E(W\otimes W)=\frac{D\mathsf S-I}{D^2-1},
$$

where $\mathsf S$ swaps the two factors. To obtain this identity, unitary invariance restricts the average to a linear combination of $I$ and $\mathsf S$; the equations $\operatorname{Tr}Z=0$ and $\operatorname{Tr}Z^2=D$ determine the coefficients. Consequently,

$$
\mathbb E|W_{ii}|^2=\frac1{D+1},\qquad
\mathbb E|W_{ij}|^2=\frac D{D^2-1}\quad(i\ne j).
$$

The diagonal covariance also yields

$$
\mathbb E\mu^2
=\frac{D\sum_ip_i^2-(\sum_ip_i)^2}{D^2-1}
=\frac{a^2}{D^2-1}.
$$

There are $D/2$ eigenvalues of each sign. Summing the logarithmic means over all ordered pairs gives

$$
\sum_{i,j}L(p_i,p_j)
=\frac D2+\frac{Da}{\log((1+a)/(1-a))}
=Dc(a).
$$

The common off-diagonal second moment overcounts each diagonal term by $1/(D^2-1)$. Since $\sum_iL(p_i,p_i)=1$,

$$
\mathbb E\sum_{i,j}L(p_i,p_j)|W_{ij}|^2
=\frac{D^2c(a)-1}{D^2-1}.
$$

Subtracting $\mathbb E\mu^2$ proves the formula for $c_D(a)$. Also $\mathbb E\rho_U=I/D$, so $\overline m(0)=0$.

Finally, choose a unitary $V$ that exchanges the two eigenspaces of $Z$, so $VZV^\dagger=-Z$. Conjugating $\rho_U$ by $V$ changes the partition function at $t$ to that at $-t$. Haar invariance therefore gives $\overline m(t)=-\overline m(-t)$. $\square$

## A response gap at fixed evidence strength

The preceding calculation concerns a derivative, but the lower bound needs a fixed nonzero update. Lemma 1 supplies the necessary uniform remainder; no order of limits is exchanged.

**Proposition 3 (fixed-update response gap).** For every $0<a<1$, $h\ge0$, and even $D\ge2$,

$$
\operatorname{Tr}[Z\mathcal E_{hZ}(\rho_0)]
-\mathbb E_U\operatorname{Tr}[Z\mathcal E_{hZ}(\rho_U)]
\ge g(a,h),
$$

where

$$
g(a,h)=[1-c(a)]h-\frac{14}{3}h^3.
$$

**Proof.** Smoothness and the uniform bound in Lemma 1 justify differentiating under the Haar integral. Oddness gives $\overline m''(0)=0$, and Taylor's theorem gives

$$
\overline m(h)
\le c_D(a)h+\frac{26}{6}h^3
\le c(a)h+\frac{13}{3}h^3.
$$

On the other hand, $\tanh h\le h$ implies

$$
(\tanh h)'=1-\tanh^2h\ge1-h^2,
$$

so $\tanh h\ge h-h^3/3$. Subtract the two bounds. $\square$

For the fixed choices $a=4/5$ and $h=1/10$,

$$
g_*:=g(4/5,1/10)
=\frac1{10}\left(\frac12-\frac{4}{5\log9}\right)
-\frac7{1500}
>0.0089237.
$$

This bound holds at every even dimension. It is a gap between the maximally mixed output response and the Haar-averaged alternative response. The proof does not require an individual-typical-input statement or a concentration theorem.

