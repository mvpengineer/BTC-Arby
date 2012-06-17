
def collapse_volumes_ask(dictionary):
    ret = []
    prices = sorted(dictionary.keys())
    for price in prices:
        ret.append((price,sum(dictionary[price].values())))
    return ret    
    
def collapse_volumes_bid(dictionary):
    ret = []
    prices = reversed(sorted(dictionary.keys()))
    for price in prices:
        ret.append((price,sum(dictionary[price].values())))
    return ret
    
def portfolio_manager(portfolio,volume,price,gain):
    hysteresis = 1.2   # get each from ML Model
    base = 100.00
    outer_scale = 1.2
    inner_scale = 100.00

    gain_percentage = gain / (volume*price)
    total_price = volume * price

    portfolio_percentage = (hysteresis - outer_scale*(base ** -(inner_scale*gain_percentage)))

    acceptable_total_price = portfolio_percentage * portfolio

    if(acceptable_total_price > total_price):
        return volume

    acceptable_volume = int(acceptable_total_price / price)
    print 'acceptable total price   =   ', acceptable_total_price
    print 'gain_percentage   =   ', gain_percentage
    print 'total_price   =   ', total_price
    return acceptable_volume