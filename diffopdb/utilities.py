import glob
import lzma
import os
import warnings

import sage.rings.integer

from sage.repl.preparse import preparse


class Unavailable(LookupError):
    pass


class FileBackedOperatorFamily:

    def __init__(self, algebra, datadir, namefmt, key_from_name=None):
        self.Dop = algebra
        self.datadir = datadir
        self.namefmt = namefmt
        if key_from_name is not None:
            self._key_from_name = key_from_name

    def open(self, key):
        path = os.path.join(self.datadir, self.namefmt.format(key))
        xzpath = path + ".xz"
        if os.path.exists(path):
            if os.path.exists(xzpath):
                warnings.warn(f"found both {path} and {xzpath}")
            return open(path)
        elif os.path.exists(xzpath):
            return lzma.open(xzpath, mode='rt')
        elif os.path.lexists(path):
            raise Unavailable(key)
        else:
            raise KeyError(key)

    def _context(self):
        Dx = self.Dop.gen()
        x = self.Dop.base_ring().gen()
        return {
            str(x): x,
            str(Dx): Dx,
            "Integer": sage.rings.integer.Integer,
        }

    def __getitem__(self, key):
        with self.open(key) as f:
            expr = preparse("".join(l.rstrip("\r\n\\")
                                    for l in f.readlines()))
        return eval(expr, self._context())

    def _key_from_name(self):
        raise NotImplementedError

    def __keys(self, full=True):
        names = glob.iglob("*", root_dir=self.datadir, recursive=True)
        return [self._key_from_name(name)
                for name in names
                if full or os.is_file(os.path.join(self.datadir, name))]

    def keys(self):
        return self.__keys(full=True)

    def available_keys(self):
        return self.__keys(full=False)
