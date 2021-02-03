from os import sep
import simulation


picks = []
sim = []
slots_total = {}
with open("appe_simulation.csv") as f:
    for i, line in enumerate(f):           
        l = line.rstrip().split(sep=",")
        picks.append(l)

with open("num_spots.csv") as f:
    for i, line in enumerate(f):           
        l = line.rstrip().split(sep=",")
        slots_total[l[0]] = l[1]

num_sim = 10000
popularity_cutoff = 124
distribution = simulation.calculate_popularity_rating(picks, slots_total, popularity_cutoff)
results = simulation.simulate_picking(picks, distribution, num_sim, slots_total)
simulation.print_data(picks, results)
print()
simulation.print_popularity_report(distribution)

print()
print(f'Number of simulations,{num_sim}')
print(f'Popularity rating cutoff,{popularity_cutoff}')
