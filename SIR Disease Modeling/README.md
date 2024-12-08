## Introduction
The SIR model or Susceptible-Infectious-Recovered model is a mathematical model that is widely used in the study of how diseases spread through populations. 
SIR model describes the dynamics of an infectious disease outbreak over time. 
Understanding the dynamics of such outbreaks has been crucial for implementing effective control measures. 
To address this challenge, mathematicians have developed the SIR model, 
a powerful tool that simplifies the complex processes of disease transmission into a set of mathematical equations. 
By analyzing these equations and the resulting model outputs, we gain valuable insights into how diseases spread within a population, 
allowing us to predict outbreak trends and inform public health interventions. 
## Basics
The model works by dividing the entire population into three categories: 
1. **Susceptible (S):** Individuals who are unaffected now but are vulnerable to getting infected 
2. **Infectious (I):** Individuals who are currently infected and are able to spread the disease 
3. **Recovered or Removed (R):** Individuals who have recovered from the disease or who have passed away from the disease. 

The model then traces the movement of individuals between these compartments over time, 
typically measured in days or weeks to provide valuable insights about the spread of the disease

## Parameters

### Disease Parameters
1. **β (Transmission Rate):** average number of people an infected individual will transmit the disease to per unit time.  
2. **γ (Recovery Rate):** rate at which infected individuals recover and move to the recovered compartment. Inverse of the average infectious period.

### Size Parameters
1. **S:** total number of individuals in the population susceptible to catching the disease.  
2. **I:** total number of individuals in the population who are currently infected and can spread the disease.  
3. **R:** total number of individuals in the population who are recovered or have passed away due to the disease and are considered no longer susceptible to the disease.  

### Initial Conditions
1. **Initial Conditions:** The model starts with specified initial numbers of susceptible (S₀), infected (I₀), and recovered (R₀) individuals.  
2. **N (Total Population Size):** total number of individuals in the population being modeled. It's used to calculate proportions of susceptible, infected, and recovered individuals.

### Transitions
1. Susceptible (S) to Infected (I) — **β**  
2. Infected (I) to Recovered (R) — **γ**  
There are no direct transitions between Susceptible (S) and Recovered (R) in the basic SIR model.

## Running Simulations
The simulation will be run with different values for recovery and transmission rates ([parameters](https://github.com/harigovindr2003/projects/tree/main/SIR%20Disease%20Modeling/parameters.csv)) to study their effects on disease spread. The total population is assumed to be 1000 individuals and simulation time is taken as 100 days for convenience. Effect of the number of initial infected individuals will be observed by first running the simulation with less I0, say 10 individuals, then say a higher I0 of say 100. Here are the [inferences](https://github.com/harigovindr2003/projects/tree/main/SIR%20Disease%20Modeling/inferences.md)
