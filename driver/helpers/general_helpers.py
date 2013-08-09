import datetime

def mtgox_timestamp_to_python(mtgox_ts):
    nineteen_seventy = datetime.datetime.utcfromtimestamp(0)
    ts = nineteen_seventy + datetime.timedelta(microseconds = mtgox_ts)
    return ts
    
def python_timestamp_to_mtgox(python_ts):
    nineteen_seventy = datetime.datetime.utcfromtimestamp(0)
    ts = python_ts - nineteen_seventy
    ts_micro = int(ts.total_seconds() * 1000000.0)
    return ts_micro