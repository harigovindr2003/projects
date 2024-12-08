## Case 1, High Transmission & Low Recovery
![](https://github.com/harigovindr2003/projects/blob/main/SIR%20Disease%20Modeling/results/case1_graph.png)
```
Basic Reproduction Number (R0): 3.00
Peak infection time: 12th day
Peak infection size: 343 individual(s)
Number of people recovered: 968 individual(s)
Percentage of total population infected at peak: 34 %
Final epidemic size: 968 individual(s)
Attack Rate: 96.80%
Number of people infected at the end of the simulation: 0 individual(s)
Herd Immunity Threshold: 66.67%
Duration of epidemic: 39 day(s)
Highest Infection Rate: 53 individual(s) infected per day
The disease does not get to 50% of the population at any given time
```
The simulation depicts a concerning scenario of a highly transmissible and slow-recovery disease with a Basic Reproduction Number (R0) of 3.00. The prolonged duration of 39 days is attributed to the combination of the high transmission rate, resulting in the disease spreading to a significant portion of the population. The peak infection on the 12th day affected 34% of individuals, with a strikingly high Attack Rate of 96.80%.The slow recovery is evident in the sustained peak infection size of 343 individuals.

## Case 2, Low Transmission & Low Recovery
![](https://github.com/harigovindr2003/projects/blob/main/SIR%20Disease%20Modeling/results/case2_graph.png)
```
Basic Reproduction Number (R0): 1.00
Peak infection time: 0th day
Peak infection size: 10 individual(s)
Number of people recovered: 136 individual(s)
Percentage of total population infected at peak: 1 %
Final epidemic size: 136 individual(s)
Attack Rate: 13.60%
Number of people infected at the end of the simulation: 1 individual(s)
Herd Immunity Threshold: 0.00%
Disease spread does not end in the given simulation period
Highest infection rate is less than 0, so not significant
The disease does not get to 50% of the population at any given time
```
The simulation demonstrates a noteworthy reduction in the Basic Reproduction Number (R0) from 3 to 1, indicating a substantial decrease in the disease's transmission rate. Despite this lower transmission, the disease persists in the population for an extended period, surpassing 100 days. In contrast, a previous simulation with a higher transmission rate concluded on the 39th day.This discrepancy underscores the significant impact of transmission rates on the disease's duration.The lower R0, while indicative of a weaker disease, paradoxically leads to a more prolonged presence within the population. Understanding these dynamics is crucial for devising effective strategies to manage and mitigate the impact of diseases with varying transmission rates.

## Case 3, Low Transmission & Low Recovery
![](https://github.com/harigovindr2003/projects/blob/main/SIR%20Disease%20Modeling/results/case3_graph.png)
```
Basic Reproduction Number (R0): 0.33
Peak infection time: 0th day
Peak infection size: 10 individual(s)
Number of people recovered: 14 individual(s)
Percentage of total population infected at peak: 1 %
Final epidemic size: 14 individual(s)
Attack Rate: 1.40%
Number of people infected at the end of the simulation: 0 individual(s)
Herd Immunity Threshold: -200.00%
Duration of epidemic: 4 day(s)
Highest infection rate is less than 0, so not significant
The disease does not get to 50% of the population at any given time
```
In this simulation, the disease exhibits a remarkably low Attack Rate of 1.4%, culminating in its swift resolution within just 4 days.The minimal impact is attributed to the combination of a low Basic Reproduction Number (R0) of 0.33, signifying a modest transmission rate, and a higher recovery rate.This concise duration and limited spread underscore the effectiveness of these factors in rapidly containing and resolving the disease within the population.

## Case 4, High Transmission & High Recovery
![](https://github.com/harigovindr2003/projects/blob/main/SIR%20Disease%20Modeling/results/case4_graph.png)
```
Basic Reproduction Number (R0): 1.00
Peak infection time: 0th day
Peak infection size: 10 individual(s)
Number of people recovered: 147 individual(s)
Percentage of total population infected at peak: 1%
Final epidemic size: 147 individual(s)
Attack Rate: 14.70%
Number of people infected at the end of the simulation: 0 individual(s)
Herd Immunity Threshold: 0.00%
Duration of epidemic: 35 day(s)
Highest infection rate is less than 0, so not significant
The disease does not get to 50% of the population at any given time
```
In this scenario, the disease presents a Basic Reproduction Number (R0) of 1.00, reflecting a moderate transmission rate.The peak infection, occurring on the 0th day, affects 1% of the population (10 individuals), with a final epidemic size of 147 individuals.The Attack Rate is 14.70%, and notably, the disease concludes within 35 days. Although the Attack Rate is relatively higher compared to previous simulations, the duration of the epidemic is shorter, indicating a balance between transmission and recovery rates. Comparing this scenario with previous simulations, where lower R0 values led to swift resolutions, this intermediate R0 results in a more extended but still manageable epidemic.The higher Attack Rate suggests increased spread, yet the effectiveness of recovery mechanisms curtails the overall impact.The absence of infections at the simulation's end, coupled with the disease not reaching 50\% of the population at any time, emphasizes the controlled nature of the outbreak.This contrast highlights the dynamic interplay between transmission and recovery rates in shaping the trajectory and severity of simulated epidemics.

## Case 5, Higher I0
![](https://github.com/harigovindr2003/projects/blob/main/SIR%20Disease%20Modeling/results/case5_graph.png)
```
Basic Reproduction Number (R0): 1.00
Peak infection time: 0th day
Peak infection size: 100 individual(s)
Number of people recovered: 401 individual(s)
Percentage of total population infected at peak: 10 %
Final epidemic size: 401 individual(s)
Number of people infected at the end of the simulation: 0 individual(s)
Attack Rate: 40.10%
Herd Immunity Threshold: 0.00%
Duration of epidemic: 26 day(s)
Highest infection rate is less than 0, so not significant
The disease does not get to 50% of the population at any given time
```
A larger initial infected population leads to an immediate and substantial peak infection size (10% of the population) with a higher Attack Rate (40.10%).The outbreak is relatively short-lived (26 days) due to the significant early transmission.The final epidemic size matches the number of people who recover (401 individuals), indicating a swift resolution.

## Case 6, Lower I0
![](https://github.com/harigovindr2003/projects/blob/main/SIR%20Disease%20Modeling/results/case6_graph.png)
```
Basic Reproduction Number (R0): 1.00
Peak infection time: 0th day
Peak infection size: 10 individual(s)
Number of people recovered: 136 individual(s)
Percentage of total population infected at peak: 1 %
Final epidemic size: 136 individual(s)
Number of people infected at the end of the simulation: 0 individual(s)
Attack Rate: 13.60%
Herd ImmunityThreshold: 0.00%
Duration of epidemic: 50 day(s)
Highest infection rate is less than 0, so not significant
The disease does not get to 50% of the population at any given time
```
A smaller initial infected population results in a more controlled outbreak, with a peak infection size of 1% of the population and a lower Attack Rate (13.60%).The epidemic duration is extended to 50 days, suggesting a slower but manageable spread.The final epidemic size exceeds the initial infected population, emphasizing a prolonged but contained outbreak.
