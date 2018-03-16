from pyhealthz import psdata
from time import localtime, strftime


def get_healthz():
    all_stats = {}
    # Record request timestamp and add to return dict
    all_stats["timestamp"] = strftime('%Y-%m-%dT%H:%M:%S',localtime())
    cpu_stats = get_cpu_stats()        
    vm_stats = get_virtualmemory_stats()
    # Get disk stats and combine
    disk_stats = get_disk_usage_stats('/')
    disk_parts = get_disk_partition_stats()
    disk_io = get_disk_io_stats()
    disk_combined = {}
    disk_combined["disk_stats"] = {}
    disk_combined["disk_stats"] = {**disk_stats, **disk_parts, **disk_io}
    net_stats = get_net_stats()
    proc_stats = get_proc_stats()
    # Merge all dicts into one
    all_stats = {**all_stats, **cpu_stats, **vm_stats, **disk_combined, **net_stats, **proc_stats}
    return all_stats

def get_cpu_stats():
    cpu_stats = psdata.get_single_cpu_pct_all_states()
    return cpu_stats

def get_virtualmemory_stats():
    vm_stats = psdata.get_virtual_memory_stats()
    return vm_stats

def get_disk_usage_stats(path = None):
    disk_stats = psdata.get_disk_usage_stats(path)
    return disk_stats

def get_disk_partition_stats():
    disk_parts = psdata.get_disk_partitions()
    return disk_parts

def get_disk_io_stats():
    disk_io = psdata.get_disk_io_stats()
    return disk_io

def get_net_stats():
    net_stats = psdata.get_net_stats()
    return net_stats

def get_proc_stats():
    proc_stats = psdata.get_proc_stats()
    return proc_stats
