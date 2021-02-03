# APPE Monte Carlo Analysis

Monte Carlo simulation of APPE regional draft to determine the probability of 
each lottery number getting their 1st, 2nd, and 3rd region picks 

## Background

Students were asked to voluntarilly share their 1st, 2nd, and 3rd region pick 
in a spreadsheet so other students could gauge the popularity of each region. 
The problem here is not everyone volunteered their picks so obtaining a 
good representation of the population becomes a bit more complex

## Methodology

First analyze the input data to create a distribution of region popularity for 
1st, 2nd, and 3rd pick, a popularity rating. Second, use the distribution to 
generate inferences for individuals that did not fill in their picks. Third, 
perform a simulation of the draft using the inferred data and store the 
results. Repeat this process n number of times (10000 was used here) and output 
the results to a csv file.

## Considerations / Biases

Individuals with a later draft number may feel less inclined to pick more 
popular regions and opt for less popular regions. This could affect our 
popularity rating.

Solution: The nature of how this is implemented makes this hard to account for, 
popularity rating would need to be recalculated for each student.

Alternative Solution: Add a cutoff for poplarity calculation of around half and 
base simulations off of the adjusted popularity rating


## Results

Can be found in the reports folder