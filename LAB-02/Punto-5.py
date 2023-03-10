def Pol5(**kwargs):
    import numpy as np

    def add_lists(a, b):
        r = []
        if len(a) >= len(b):
            for i in range(len(a)):
                r.append(0)
        elif len(b) > len(a):
            for i in range(len(b)):
                r.append(0)
        if len(a) > len(b):
            for i in range(len(b)):
                r[i] = a[i] + b[i]
            for i in range(len(b), len(a)):
                r[i] = a[i]
        elif len(b) > len(a):
            for i in range(len(a)):
                r[i] = a[i] + b[i]
            for i in range(len(a), len(b)):
                r[i] = b[i]
        elif len(a) == len(b):
            for i in range(len(r)):
                r[i] = a[i]+b[i]
        return r

    class Pol5__class:

        def __init__(self):
            self.coefs = [0]

        def add_term(self, c, e):
            if e > len(self.coefs):
                for i in range(len(self.coefs), e+1):
                    self.coefs.append(0)
            value = self.coefs[e]
            self.coefs[e] = c + value
            return self

            return self

        def sum(self, q):
            r = self.__class__()
            r.coefs = add_lists(self.coefs, q.coefs)
            return r

        def show(self):
            from IPython.display import Math, HTML, display
            display(HTML(
                "<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
            s = "+".join(["%s^{%s}" % (str(c) if e == 0 else str(c)+"x" if c != 1 else "x", str(
                e) if e not in [0, 1] else "") for e, c in enumerate(self.coefs) if c != 0])
            s = s.replace("+-", "-")
            return Math(s)

    return Pol5__class(**kwargs)


p = Pol5()
p.add_term(3, 2).add_term(2, 1).add_term(4, 5).add_term(6, 2)
p.show()

# 2x + 9x^2 + 4x^5

q = Pol5()
q.add_term(1, 5).add_term(4, 1).add_term(3, 8)
q.show()

# 4x + x^5 + 3x^8

s = p.sum(q)
print(s.coefs)
s.show()
