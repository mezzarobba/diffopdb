r"""
Batyrev-Kreuzer periods

Data from https://mathexp.eu/lairez/supp/periods/, courtesy of Pierre Lairez.

This modules provides the annihilating operators of the 210 principal periods
given in *Constructing new Calabi-Yau 3-folds and their mirrors via conifold
transitions* (Batyrev and Kreuzer, 2010, In: Adv. Theor. Math. Phys. 14.3), using the same numbering as:

http://hep.itp.tuwien.ac.at/~kreuzer/math/0802/

EXAMPLES::

    sage: import btp
    sage: btp.keys()
    [(10, 1649),
     (10, 1770),
     (10, 1777),
     ...
    ]
    sage: btp.dop(13, 3754)
    (t^13 + 479/40*t^11 - 26659/6400*t^9 - 241/640*t^7 + 69069/409600*t^5 -
    441/409600*t^3)*Dt^4 + (14*t^12 + 583/5*t^10 - 203331/3200*t^8 +
    2879/1280*t^6 + 67053/40960*t^4 - 1323/204800*t^2)*Dt^3 + (54*t^11 +
    11111/40*t^9 - 336737/1600*t^7 + 162641/5120*t^5 + 1642011/409600*t^3 -
    3087/409600*t)*Dt^2 + (60*t^10 + 1479/10*t^8 - 9263/64*t^6 +
    262861/5120*t^4 + 983493/409600*t^2 - 441/409600)*Dt + 12*t^9 + 91/20*t^7 -
    609/160*t^5 + 13629/1280*t^3 + 441/2560*t
"""

import lzma
import os

import sage.rings.integer

from sage.repl.preparse import preparse
from sage.rings.all import QQ, PolynomialRing

from ore_algebra import OreAlgebra

data_dir = os.path.join(os.path.dirname(__file__), "data/")

Pol = PolynomialRing(QQ, "t")
Dop = OreAlgebra(Pol, "Dt")

def keys(*, available=False):
    full = not available
    return [tuple(int(a) for a in name.split('.')[1:3])
            for name in os.listdir(data_dir)
            if full or os.is_file(os.path.join(data_dir, name))]

def _lines(x, y):
    path = os.path.join(data_dir, f"dop.{x}.{y}")
    if os.path.exists(path):
        with open(path) as f:
            return f.readlines()
    path += ".xz"
    if os.path.exists(path):
        with lzma.open(path, mode='rt') as f:
            return f.readlines()
    elif os.path.lexists(path):
        raise RuntimeError("not available locally")
    raise KeyError(f"unknown operator {x}.{y}")

def dop(x, y):
    lines = _lines(x, y)
    expr = preparse("".join(l.rstrip("\r\n\\") for l in lines))
    context = {
        "t": Pol.gen(),
        "D": Dop.gen(),
        "Integer": sage.rings.integer.Integer,
    }
    try:
        return eval(expr, context)
    except SyntaxError as exn:
        print(exn.offset, expr[exn.offset-10:exn.offset+10])
        raise RuntimeError()
