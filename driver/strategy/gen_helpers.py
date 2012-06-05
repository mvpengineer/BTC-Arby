
def collapse_volumes_ask(dictionary):
    """
    take all the volumes at one price and add them, sort in the order of asks, which is ascending.
    """
    ret = []
    prices = sorted(dictionary.keys())
    for price in prices:
        ret.append((price,sum(dictionary[price].values())))
    return ret    
    
def collapse_volumes_bid(dictionary):
    """
    take all the volumes at one price and add them, sort in the order of bids, which is descending.
    """
    ret = []
    prices = reversed(sorted(dictionary.keys()))
    for price in prices:
        ret.append((price,sum(dictionary[price].values())))
    return ret
    
def portfolio_manager(portfolio_start, portfolio_now,volume,price,gain):
    """
    Determines how much of the portfolio to invest in a single idea.  Depending on the percent gain, we invest more.  
    """
    hysteresis = 1.2   # get each from ML Model
    base = 100.00
    outer_scale = 1.2
    inner_scale = 100.00
    
    total_price = volume * price    
    gain_percentage = gain / (total_price)

    portfolio_percentage = (hysteresis - outer_scale*(base ** -(inner_scale*gain_percentage)))
                #check out this equation on wolfram alpha with the query: (1.2 - 1.2*(100 ^ -(100*x))) from 0 to .005
                #x axis is percentage gain, y is portfolio percentage that can be used

    acceptable_total_price = portfolio_percentage * portfolio_start
    
    portfolio_currently_invested = portfolio_start - portfolio_now
    acceptable_total_price -= portfolio_currently_invested              #account for money already invested.  if you have 100 $, and we are willing to invest 10, but we've already invested 6, we are only willing to invest 4.
    
    if(acceptable_total_price <= 0):
        return 0
    
    if(acceptable_total_price > total_price):   #if we're willing to invest more than is possible at current volume, invest all
        return volume
                                                #else, invest the amount we're willing to based on the percentage
    acceptable_volume = int(acceptable_total_price / price)
    
    return acceptable_volume