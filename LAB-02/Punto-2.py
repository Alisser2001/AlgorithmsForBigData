def Pol2(**kwargs):
    import numpy as np

    class Pol2__class:

        def __init__(self):
            self.exps = []
            self.coefs = []

        def len(self):
            return len(self.exps)

        def add_term(self, c, e):
            if e not in self.exps:
                if len(self.coefs) == 0:
                    self.coefs.append(c)
                    self.exps.append(e)
                else:
                    i = np.searchsorted(self.exps, e)
                    self.coefs.insert(i, c)
                    self.exps.insert(i, e)

            elif e in self.exps:
                i = self.exps.index(e)
                value = self.coefs[i]
                self.coefs[i] = c + value

            assert len(self.exps) == len(
                self.coefs), "must have the same number of exps and coefs"
            return self

        def sum(self, q):
            r = self.__class__()
            r.exps = self.exps
            r.coefs = self.coefs
            for c, e in zip(q.coefs, q.exps):
                if e not in r.exps:
                    i = np.searchsorted(self.exps, e)
                    r.exps.insert(i, e)
                    r.coefs.insert(i, c)
                else:
                    i = self.exps.index(e)
                    value = self.coefs[i]
                    self.coefs[i] = c + value
            return r

        def show(self):
            from IPython.display import Math, HTML, display
            display(HTML(
                "<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
            s = "+".join(["%s^{%s}" % (str(c) if e == 0 else str(c)+"x" if c != 1 else "x", str(
                e) if e not in [0, 1] else "") for e, c in zip(self.exps, self.coefs) if c != 0])
            s = s.replace("+-", "-")
            return Math(s)

    return Pol2__class(**kwargs)


p = Pol2()
p.add_term(3, 2).add_term(2, 1).add_term(4, 5).add_term(6, 2)
p.show()

# 2x+9x^2+4x^5

q = Pol2()
q.add_term(1, 5).add_term(4, 1).add_term(3, 3)
q.show()

# 4x+3x^3+x^5

p.sum(q).show()

# 6x+9x^2+3x^3+5x^5
