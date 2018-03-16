import psutil

def get_single_cpu_pct_all_states():
    #  Get snapshot of current cpu usage %, then split out user, system
    rtn = {}
    cpu_stats = psutil.cpu_times_percent(1)
    rtn = psutil_result_parser(str(cpu_stats), 'cpu_total')
    return rtn

def get_virtual_memory_stats():
    rtn = {}
    vm_stats = psutil.virtual_memory()
    rtn = psutil_result_parser(str(vm_stats), 'virtual_memory')
    return rtn

def get_disk_usage_stats(path='/'):
    rtn = {}
    disk_stats = psutil.disk_usage(path)
    rtn = psutil_result_parser(str(disk_stats), 'disk_usage')
    return rtn

def get_disk_partitions():
    rtn = {}
    disk_parts = psutil.disk_partitions()
    rtn = psutil_result_parser(str(disk_parts), 'disk_partitions')
    return rtn

def get_disk_io_stats():
    rtn = {}
    disk_io = psutil.disk_io_counters()
    rtn = psutil_result_parser(str(disk_io), 'disk_iostats')
    return rtn

def get_net_stats(pernic = True):
    rtn = {}
    rtn["network_stats"] = {}
    net_stats = psutil.net_io_counters(pernic)
    # net_io_counters returns a dict where key == nic and value is a psutil object that needs parsing
    print(f'net_stats ---> {str(net_stats)}')
    for nic in net_stats:
        print(f'NIC ---> {str(nic)}')
        rtn["network_stats"][nic] = psutil_result_parser(str(net_stats[nic]), 'network_stats')
    return rtn

def get_proc_stats():
    rtn = {}
    rtn["process_count"] = str(len(psutil.pids()))
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
