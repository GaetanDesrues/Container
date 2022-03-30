import os.path

import treefiles as tf


class Ct:
    def __init__(self, path):
        self.root = tf.Tree(path)
        self.meta_fname = self.root / "metadata.json"
        if not tf.isfile(self.meta_fname):
            self.root.dump()
            self.metadata = {}
            self.data = {}
            self.fnames = {}
        else:
            d = tf.load_json(self.meta_fname)
            self.metadata = d["metadata"]
            self.data = d["data"]
            self.fnames = d["fnames"]

    def __truediv__(self, other):
        r = tf.Str(self.root) / other
        self.fnames.update({os.path.splitext(other)[0]: r})
        return r

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        d = {"metadata": self.metadata, "data": self.data, "fnames": self.fnames}
        tf.dump_json(self.meta_fname, d)
        tf.logf(self.meta_fname)

    def add(self, **kw):
        self.data.update(kw)

    def __getattr__(self, item):
        if item in self.fnames:
            return self.fnames[item]
        elif item in self.data:
            return self.data[item]
        else:
            super().__getattribute__(item)

    def __repr__(self):
        s = f"Meta data:\n{self.metadata}\n"
        s += "Fnames: \n"
        for x, y in self.fnames.items():
            s += f"  - {x}: {y}\n"
        s += f"Data:\n{self.data}\n"
        return s
