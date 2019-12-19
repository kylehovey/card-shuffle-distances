# Optimal Shuffle Distance
_Kyle Hovey_

---

This problem pertains to a deck of cards, but more abstractly to an ordered list of distinguishable elements and a metric over the space of possible permutations.

Define a deck $D$ of size $n$ to be an ordered list of $n$ cards. Define a shuffle $\psi$ to be any action that takes a deck $D$ to another deck $\hat{D} \equiv \psi(D)$ that contains all of the same elements of $D$, but not necessarily in the same order. That is:

>$\psi:\mathbb{D}_n\rightarrow\mathbb{D}_n \ni c \in D \iff c \in \hat{D} \quad \forall c \in D$

where $\mathbb{D}_n$ is the space of all possible decks of size $n$.

## First Problem:

Define a metric $<\cdot,\cdot>:\mathbb{D}_n^2\rightarrow\mathbb{R}$ that measures the sum of the absolute distances each element "traveled" in the shuffle. More formally:

>$<D,\hat{D}> \ \equiv \displaystyle \sum_{k=1}^n |I(c_k) - I(\hat{c_k})|$

where $\hat{c_k}$ is $c_k$ in the shuffled deck, and $I(c_k)$ gives the ordered index of card $k$.

1. *Given $n$, find $\psi$ that maximizes $<D,\hat{D}>$.*

## Second Problem:

Define a metric $<\cdot,\cdot>:\mathbb{D}_n^2\rightarrow\mathbb{R}$ that measures the sum of the absolute distances each element "traveled" in the shuffle _from its neighbors_. If the original cards were on the outside of the deck, then just measure the distance it traveled from its one adjacent neighbor. More formally:

>$<D,\hat{D}> \ \equiv$

>$\qquad |I(c_1) - I(\hat{c_2})|$

>$\qquad + \ \Big(\displaystyle \sum_{k=2}^{n-1} |I(c_k) - I(\hat{c_{k - 1}})| + |I(c_k) - I(\hat{c_{k+1}})|\Big)$

>$\qquad + \ |I(c_{n - 1}) - I(\hat{c_n})|$

where $\hat{c_k}$ is $c_k$ in the shuffled deck, and $I(c_k)$ gives the ordered index of card $k$.

2. *Given $n$, find $\psi$ that maximizes $<D,\hat{D}>$.*
