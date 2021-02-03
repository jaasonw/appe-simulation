import copy
import random

def pick(picks, slots):
    sim = []
    slots_total = slots.copy()
    for person in picks:
        pick = "LITERALLY AUTOFILLED"
        for choice in person:
            if len(choice) < 1:
                pick = "DIDN'T PICK"
                break
            elif int(slots_total[choice]) > 0:
                slots_total[choice] = int(slots_total[choice]) - 1
                pick = choice
                break
        sim.append(pick)
    return sim

def calculate_popularity_rating(picks, slots_total, cutoff=-1):
    slots_probability = [{}, {}, {}]
    cutoff = len(picks) if cutoff == -1 else cutoff
    for i in range(0, len(slots_probability)):
        for key, value in slots_total.items():
            num = 0
            for j in range(0, cutoff):
                if picks[j][i] == key:
                    num += 1
            slots_probability[i][key] = num / len(picks)
    return slots_probability


def generate_simulation(picks, popularity_distrubution):
    population = popularity_distrubution[0].keys()
    sim = copy.deepcopy(picks)
    for person in sim:
        for i in range(0, len(person)):
            weights = popularity_distrubution[i].values()
            if person[i] == "":
                person[i] = random.choices(list(population), list(weights))[0]
    return sim

def simulate_picking(picks, popularity_distrubution, num, slots_total):
    results = []
    simulations = []
    for i in range(0, len(picks)):
        simulations.append({})
        for key in slots_total.keys():
            simulations[i][key] = 0

    for i in range(0, num):
        simulated_picks = generate_simulation(picks, popularity_distrubution)
        sim = pick(simulated_picks, slots_total)
        for i in range(0, len(sim)):
            if sim[i] in simulations[i]:
                simulations[i][sim[i]] += 1
    for e in simulations:
        for key, value in e.items():
            e[key] = (value / num) * 100
        results.append(e)
    return results

def print_data(picks, results):
    for i in range(0, len(picks)):
        for choice in picks[i]:
            if choice in results[i]:
                print(f'{choice} ({results[i][choice]:.2f})', end=",")
            else:
                print("N/A", end=",")
        print()

def print_popularity_report(popularity_rating):
    for key, _ in popularity_rating[0].items():
        print(key,end=",")
    print()
    for e in popularity_rating:
        for _, value in e.items():
            print(value,end=",")
        print()