from time_simulator import *

class Organism(object):
    hysteresis = 1.2
    base = 100.00
    outer_scale = 1.2
    inner_scale = 100.00
    profit = 0
    
    def get_profit(self):
        return profit
    def get_profit(self,prof):
        self.profit = prof
    
def max_profit(organisms):
    max_prof = organisms[0].get_profit()
    max_org = organisms[0]
    for organism in organisms:
        org_prof = organism.get_profit()
        if  org_prof > max_prof:
            max_prof = org_prof
    return (max_prof,max_org)

def drive():
    end_profit = 1000.00
    num_organisms = 100
    variance = .1
    organisms = []
    for i in range(num_organisms):
        organisms.append(Organism)
    num_generations = 0
    (current_prof,current_org) = max_profit(organisms)
    while( < end_profit and num_generations < 10000):
        for organism in organisms:
            simulate(organism)
        organisms = next_gen(organisms,variance)
        
        (current_prof,current_org) = max_profit(organisms)
        if num_generations % 100 == 0:
            variance -= .01
        num_generations += 1
    return current_org

def next_gen(organisms,variance):
    num_organisms_to_start = 10
    next_gen_orgs = []
    breeded_orgs = []
    for i in range(num_organisms_to_start):
        (current_prof,current_org) = max_profit(organisms)
        next_gen_orgs.append(current_org)
        organisms.remove(current_org)
    for organism_one in next_gen_orgs:
        for organism_two in next_gen_orgs:
            breeded_orgs.append(breed(organism_one,organism_two,variance))
    return breeded_orgs
    
def breed(one,two,variance):
    var = math.sqrt(one.var * two.var)
    rand_perc = random.uniform(-variance,variance)
    var *= (1+rand_perc)
    
    
    
    
    
    