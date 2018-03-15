import psutil

def get_single_cpu_pct_all_states():
    #  Get snapshot of current cpu usage %, then split out user, system
    rtn = {}
    cpu_stats = psutil.cpu_times_percent(1)
    rtn = psutil_result_parser(str(cpu_stats), 'cpu_total')
    return rtn

def psutil_result_parser(psutil_stats, keyname):
    # Different systems will report different cpu states, so keep a dict to be referenced implicitly
    return_list = {}
    try:
        breakdown = psutil_stats.split('(')[1][:-1]
        return_list[keyname] = {}
        for stat in breakdown.split(','):
            stat_split = stat.split('=')
            return_list[keyname][stat_split[0].strip()] = stat_split[1].strip()
    finally:
        return return_list
