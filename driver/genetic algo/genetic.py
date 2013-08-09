from time_simulator import *

class Organism(object):
    hysteresis = 1.2
    base = 100.00
    outer_scale = 1.2
    inner_scale = 100.00
    profit = 0
    
    def get_profit(self):
        return profit
    
    def set_profit(self,prof):
        self.profit = prof
    
def max_profit(organisms):
    """
    Who is the fittest organism measured by money makings
    """
    max_prof = organisms[0].get_profit()
    max_org = organisms[0]
    for organism in organisms:
        org_prof = organism.get_profit()
        if  org_prof > max_prof:
            max_prof = org_prof
            max_org = organism
    return (max_prof,max_org)

def drive():
    """
    Start with 100 organisms, simulate against the history, and finally, create the next generation of organisms.
    """
    end_profit = 1000.00    #the amount of money that would end the simulation, basically, an error threshold
    num_organisms = 100
    num_generations = 10000
    variance = .1
    levels_of_variance = 10.0
    organisms = []
    for i in range(num_organisms):
        organisms.append(Organism())
    num_generations = 0
    (current_prof,current_org) = max_profit(organisms)
    while(current_prof < end_profit and num_generations < num_generations):
        for organism in organisms:
            simulate(organism)
        organisms = next_gen(organisms,variance)
        
        (current_prof,current_org) = max_profit(organisms)
        if num_generations % num_generations/levels_of_variance == 0:
            variance -= variance/levels_of_variance     #every 100 generations, decrease the variance by this amount, this will affect the breed function
        num_generations += 1
    return current_org

def next_gen(organisms,variance):
    """
    Take the 100 organisms, find the max 10 of them, and then breed them with each other, creating 100 again.
    """
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
    """
    Take two organisms and determine a new organism--for each variable, multiply the var from each organism, and sqrt.  
    Then add a random amount from 0 -> variance percentage to each var.
    """
    var = math.sqrt(one.var * two.var)
    rand_perc = random.uniform(-variance,variance)
    var *= (1+rand_perc)
    
    
    
    
    
    