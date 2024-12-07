import numpy as np
import matplotlib.pyplot as plt
# Define SIR model parameters
beta = float(input("Enter the transmission rate: "))
gamma = float(input("Enter the recovery rate: "))
N = float(input("Enter the total population size: "))
T = max(1, int(input("Enter Simulation time in Days (T): ")))
I0 = float(input("Enter the initial
number of infected population: "))
t = np.linspace(0, T, 100)
# Solve SIR equations using Euler’s method
S = np.zeros(len(t))
I = np.zeros(len(t))
R = np.zeros(len(t))
S[0] = N
I[0] = I0
R[0] = 0
for i in range(1, len(t)):
dS = -beta * S[i-1] * I[i-1] / N
dI = beta * S[i-1] * I[i-1] / N - gamma * I[i-1]
dR = gamma * I[i-1]
S[i] = S[i-1] + dS
I[i] = I[i-1] + dI
R[i] = R[i-1] + dR
# Plot the results
plt.plot(t, S, label=’Susceptible’)
plt.plot(t, I, label=’Infected’)
plt.plot(t, R, label=’Recovered’)
plt.xlabel(’Time’)
plt.ylabel(’Population’)
plt.title(’SIR Model Simulation’)
plt.legend()
plt.grid(True)
plt.show()
# Calculate insights
R0 = beta / gamma
peak_infection_time = int(np.argmax(I))
peak_infection_size = int(np.max(I))
final_epidemic_size = int(R[-1])
final_infected_count = int(I[-1])
duration_of_epidemic = np.argmax(I < 1)
rate_of_change_infected = int(float(np.max(np.diff(I))))
proportion_infected = I / N
number_recovered = int(R[-1])
proportion_infected_percentage_at_peak =
int(float(f"{proportion_infected[peak_infection_time]}") * 100)
time_to_50_percent = np.argmax(proportion_infected >= 0.5)
attack_rate = (final_epidemic_size / N) * 100
herd_immunity_threshold = 1 - (1 / R0)
# Print results
print("\nRESULTS")
print(f"Basic Reproduction Number (R0): {R0:.2f}")
print(f"Peak infection time: {peak_infection_time}th day")
print(f"Peak infection size: {peak_infection_size} individual(s)")
print(f"Number of people recovered:
{number_recovered} individual(s)")
print("Percentage of total population infected at peak:",
proportion_infected_percentage_at_peak, "%")
print("Final epidemic size:", final_epidemic_size,"individual(s)")
print(f"Attack Rate: {attack_rate:.2f}%")
print(f"Number of people infected at the end of the simulation:
{final_infected_count} individual(s)")
print(f"Herd ImmunityThreshold: {herd_immunity_threshold:.2%}")
if duration_of_epidemic==0:
print("Disease spread does not end in the given simulation period")
else:
print("Duration of epidemic:", duration_of_epidemic, "day(s)")
if rate_of_change_infected==0:
print("Highest infection rate is less than 0, so not significant")
else:
print("Highest Infection Rate:", rate_of_change_infected,
"individual(s)
infected per day")
if time_to_50_percent ==0:
print("The disease does not get to 50% of
the population at any given time")
else:
print(f"Time to Reach 50% of
the Population: {time_to_50_percent} day(s)")
