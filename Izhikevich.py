from matplotlib import pyplot as plt

# a, b, c, d = [0.02, 0.2, -65, 8]
a, b, c, d = [0.02, 0.2, -50, 2]
I = 4
v = c
u = 0

def dvdt(v, u, b, I):
    return 0.04*(v**2) + 5*v + 140 - b*u + I

def dudt(v, u, a):
    return a * (v - u)

vlst = [v]
for i in range(500):
    v += dvdt(v, u, b, I)
    u += dudt(v, u, a)
    vlst.append(v)
    if v >= 30:
        v = c
        u += d

plt.plot(range(501), vlst)
plt.ylim([-90, 30])
plt.ylabel("V")
plt.xlabel("t")
# plt.title("Izhikevich - regular spiking (RS) neuron")
plt.title("Izhikevich - first-rhythmic bursting (FRB) neuron")
plt.show()