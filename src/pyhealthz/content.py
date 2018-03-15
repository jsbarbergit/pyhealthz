from pyhealthz import psdata
from time import localtime, strftime


def get_healthz():
    all_stats = {}
    all_stats["timestamp"] = strftime('%Y-%m-%dT%H:%M:%S',localtime())
    cpu_stats = get_cpu_stats()        
    all_stats = {**all_stats, **cpu_stats}    
    return all_stats

def get_cpu_stats():
    cpu_stats = psdata.get_single_cpu_pct_all_states()
    return cpu_stats
