def Pol3(**kwargs):
    import numpy as np

    class Pol3__class:

        def __init__(self):
            self.coefs = [0]

        def add_term(self, c, e):
            if e > len(self.coefs):
                for i in range(len(self.coefs), e+1):
                    self.coefs.append(0)
            value = self.coefs[e]
            self.coefs[e] = c + value
            return self

        def show(self):
            from IPython.display import Math, HTML, display
            display(HTML(
                "<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=default'></script>"))
            s = "+".join(["%s^{%s}" % (str(c) if e == 0 else str(c)+"x" if c != 1 else "x", str(
                e) if e not in [0, 1] else "") for e, c in enumerate(self.coefs) if c != 0])
            s = s.replace("+-", "-")
            return Math(s)

    return Pol3__class(**kwargs)


p = Pol3()
p.add_term(2, 0)
p.add_term(1, 5)
p.add_term(3, 2)
p.add_term(5, 5)
print(p.coefs)
p.show()

p.add_term(1, 8)
print(p.coefs)
p.show()
