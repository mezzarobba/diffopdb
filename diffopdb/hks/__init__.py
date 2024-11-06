r"""
Picard-Fuchs equations of families of quartic surfaces

https://arxiv.org/abs/2007.13786

Data courtesy of Avinash Kulkarni and Emre Sertöz.

The following text is adapted from the description they provided:

Each subdirectory in data/ corresponds to a single one-parameter family with
the fibre over 0 being the first polynomial and the fibre over 1 being the
other. For example, the directory

data/edge-ivp__x3w+x2w2+xw3+y3z+yz3__x3w+x2w2+xw3+y4+z4/

corresponds to the 1-parameter family

T * (x^3 w + x^2 w^2 + x w^3 + y^3 z+ y z^3) + (1-T) * (x^3 w + x^2 w^2 + xw^3 + y^4 + z^4)

Within this directory you'll find up to 21 different files of the form dop.$n
or dop.$n.xz where $n is a number in {1, ..., 21}. The differential equation in
that file is the Picard-Fuchs differential equation which annihilates the n-th
cohomology class on the pencil of K3's.


EXAMPLES:

    sage: from diffopdb import hks
    sage: hks.dop["x3w+x2w2+xw3+y3z+yz3__x3w+x2w2+xw3+y4+z4/dop.1"]
    (29160*t^7 - 44388*t^6 + 38736*t^5 - 21676*t^4 + 8360*t^3 - 2364*t^2 +
    416*t - 52)*D^2 + (80190*t^6 - 103680*t^5 + 90846*t^4 - 41328*t^3 +
    13050*t^2 - 2448*t + 234)*D + 18225*t^5 - 22194*t^4 + 32598*t^3 - 16080*t^2
    + 5361*t - 1014
"""

import os
from sage.rings.all import QQ, PolynomialRing
from ore_algebra import OreAlgebra
from ..utilities import FileBackedOperatorFamily

dop = FileBackedOperatorFamily(
    algebra = OreAlgebra(PolynomialRing(QQ, "t").fraction_field(),
                         ("D", lambda p: p, lambda p: p.derivative())),
    datadir = os.path.join(os.path.dirname(__file__), "data/"),
    namefmt = "edge-ivp__{0}",  # TBI...
)

