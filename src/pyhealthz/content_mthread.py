from pyhealthz import psdata
from time import localtime, strftime
from multiprocessing import Process, Queue, Pipe

# Set the path to get Disk Usage stats from
DISK_USAGE_PATH = '/'

def parallel_run(*funcs):
    # Create a dict to ld proc id and correspodning queue
    proc_details = {}
    rtn = {}
    for fn in funcs:
        # Create a queue object to receive return value
        q = Queue()
        if str(fn).split(' ')[1] == 'get_disk_usage_stats':
            p = Process(target=fn, args=(q, DISK_USAGE_PATH))
        else:
            p = Process(target=fn, args=(q,))
        p.start()
        proc_details[p] = q
    for proc in proc_details:
        # Get the dict value returned
        q = proc_details[proc]
        output = q.get()
        # merge output with overall rtn dict
        rtn = {**rtn, **output}
        # Wait for this process to finish
        proc.join()    

    return rtn


def get_healthz():
    all_stats = {}
    # Record request timestamp and add to return dict
    stats = parallel_run(get_cpu_stats, get_virtualmemory_stats, get_disk_usage_stats, get_disk_partition_stats, get_disk_io_stats, get_net_stats, get_proc_stats)
    # assemble return dict for compatibility with non threaded version
    all_stats["timestamp"] = strftime('%Y-%m-%dT%H:%M:%S',localtime())
    all_stats["cpu_total"] = stats["cpu_total"]
    all_stats["virtual_memory"] = stats["virtual_memory"]
    all_stats["disk_stats"] = {}
    all_stats["disk_stats"]["disk_usage"] = stats["disk_usage"]
    all_stats["disk_stats"]["disk_partitions"] = stats["disk_partitions"]
    all_stats["disk_stats"]["disk_iostats"] = stats["disk_iostats"]
    all_stats["network_stats"] = stats["network_stats"]
    all_stats["process_count"] = stats["process_count"]
    return all_stats

def get_cpu_stats(q):
    q.put(psdata.get_single_cpu_pct_all_states())

def get_virtualmemory_stats(q):
    q.put(psdata.get_virtual_memory_stats())

def get_disk_usage_stats(q, path=None):
    q.put(psdata.get_disk_usage_stats(path))

def get_disk_partition_stats(q):
    q.put(psdata.get_disk_partitions())

def get_disk_io_stats(q):
    q.put(psdata.get_disk_io_stats())

def get_net_stats(q):
    q.put(psdata.get_net_stats())

def get_proc_stats(q):
    q.put(psdata.get_proc_stats())
