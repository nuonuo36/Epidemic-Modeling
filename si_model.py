import matplotlib.pyplot as plt
import numpy as np

N = 1000
I0 = 100
R0 = 0
S0 = N - I0 - R0

I = [I0]
S = [S0]
R = [R0]

Dt = 1
I_previous = I0
S_previous = S0
R_previous = R0

for n in range(400):

  #add noise. loc = mean, scale = standard deviation
  b_statistic = 0.002
  b = np.random.normal(loc=b_statistic, scale=b_statistic * 0.5)

  recovering_rate_statistic = 0.15
  recovering_rate = np.random.normal(loc=recovering_rate_statistic,
                                     scale=recovering_rate_statistic * 0.1)

  S_next = S_previous - b * (
      S_previous) * I_previous * Dt - I_previous * recovering_rate * Dt
  I_next = I_previous + b * (
      S_previous) * I_previous * Dt - I_previous * recovering_rate * Dt
  R_next = R_previous + I_previous * recovering_rate * Dt

  I_previous = I_next
  S_previous = S_next
  R_previous = R_next
  I.append(I_previous)
  S.append(S_previous)
  R.append(R_previous)

#legend
plt.plot(I, "yellow")
plt.plot(S, "blue")
plt.plot(R, "green")

plt.savefig("SIR.png")
