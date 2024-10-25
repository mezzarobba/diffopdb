r"""
Batyrev-Kreuzer periods

Data from https://mathexp.eu/lairez/supp/periods/, courtesy of Pierre Lairez.

This modules provides the annihilating operators of the 210 principal periods
given in *Constructing new Calabi-Yau 3-folds and their mirrors via conifold
transitions* (Batyrev and Kreuzer, 2010, In: Adv. Theor. Math. Phys. 14.3), using the same numbering as:

http://hep.itp.tuwien.ac.at/~kreuzer/math/0802/

EXAMPLES::

    sage: from diffopdb import bkp
    sage: bkp.dop.keys()
    ['10.1649',
     '10.1770',
     '10.1777',
     ...
    ]
    sage: bkp.dop["13.3754"]
    (t^13 + 479/40*t^11 - 26659/6400*t^9 - 241/640*t^7 + 69069/409600*t^5 -
    441/409600*t^3)*Dt^4 + (14*t^12 + 583/5*t^10 - 203331/3200*t^8 +
    2879/1280*t^6 + 67053/40960*t^4 - 1323/204800*t^2)*Dt^3 + (54*t^11 +
    11111/40*t^9 - 336737/1600*t^7 + 162641/5120*t^5 + 1642011/409600*t^3 -
    3087/409600*t)*Dt^2 + (60*t^10 + 1479/10*t^8 - 9263/64*t^6 +
    262861/5120*t^4 + 983493/409600*t^2 - 441/409600)*Dt + 12*t^9 + 91/20*t^7 -
    609/160*t^5 + 13629/1280*t^3 + 441/2560*t
"""

import os

from sage.rings.all import QQ, PolynomialRing

from ore_algebra import OreAlgebra

from ..utilities import FileBackedOperatorFamily

Pol = PolynomialRing(QQ, "t")
Dop = OreAlgebra(Pol, "Dt")


dop = FileBackedOperatorFamily(
    algebra=OreAlgebra(PolynomialRing(QQ, "t"),
                       ("D", lambda p: p, lambda p: p.derivative())),
    datadir = os.path.join(os.path.dirname(__file__), "data/"),
    namefmt = "dop.{0}",
    key_from_name=lambda name: "{1}.{2}".format(*name.split(".")),
)


# A hopefully representative subset of the data, sorted roughly by total size.
# Each sublist contains operators of roughly the same size.

sel = [
    ["9.35", "7.6", "9.635"],
    ["11.3822", "11.3799", "14.3460"],
    ["25.86", "24.147", "23.1347"],
    ["20.1295", "21.2054", "21.2052"],
    ["22.986", "21.87", "21.6"],
    ["24.1344", "23.168", "24.85"],
    ["22.1484", "22.590", "21.2200"],
    ["24.94", "24.481", "25.51"],
    ["23.697", "23.674"],
    ["21.1908"],
]
