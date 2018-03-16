import pytest
import psutil
from pyhealthz import psdata

# Sad Paths
def test_psutil_result_parser_invalid_args(mocker):
    """
    Errorif invalid args passed
    """
    with pytest.raises(TypeError):
        psdata.psutil_result_parser()
        psdata.psutil_result_parser('arg1')

#Happy Paths

# Need to mock psutil
def test_single_cpu_pct_stat_psutil_call(mocker):
    """
    single data point for all cpu states should call psutil.cpu_timers_percent
    with a value of 1
    Should return list
    """
    mocker.patch('psutil.cpu_times_percent')
    assert psdata.get_single_cpu_pct_all_states()
    psutil.cpu_times_percent.assert_called_with(1)
    type(psdata.get_single_cpu_pct_all_states()) == type(dict())

def test_psutil_result_parser_returns_list():
    """
    psutil parsing function should return a dict
    even when passed an empty string
    """
    assert dict(psdata.psutil_result_parser('scputimes(user=2.0, nice=0.0, system=1.2, idle=96.8)', 'test_metric'))
    type(psdata.psutil_result_parser('','')) == type(dict())

def test_ram_stats(mocker):
    """
    test function runs and runs with 0 args
    """
    mocker.patch('psutil.virtual_memory')
    assert psdata.get_virtual_memory_stats()
    psutil.virtual_memory.assert_called_with()
    type(psdata.get_virtual_memory_stats()) == type(dict())

def test_disk_stats(mocker):
    """
    test function runs and returns with 1 arg
    """
    mocker.patch('psutil.disk_usage')
    assert psdata.get_disk_usage_stats('/')
    psutil.disk_usage.assert_called_with('/')
    type(psdata.get_disk_usage_stats('/')) == type(dict())

def test_disk_stats_noargs(mocker):
    """
    test function runs and returns with 0 args passed in
    uses default value of /
    """
    mocker.patch('psutil.disk_usage')
    assert psdata.get_disk_usage_stats()
    psutil.disk_usage.assert_called_with('/')
    type(psdata.get_disk_usage_stats()) == type(dict())

def test_disk_partitions(mocker):
    """
    test function runs and returns - no args
    """
    mocker.patch('psutil.disk_partitions')
    assert psdata.get_disk_partitions()
    psutil.disk_partitions.assert_called_with()
    type(psdata.get_disk_partitions()) == type(dict())

def test_disk_io(mocker):
    """
    test function runs and return dict - no args
    """ 
    mocker.patch('psutil.disk_io_counters')
    assert psdata.get_disk_io_stats()
    psutil.disk_io_counters.assert_called_with()
    type(psdata.get_disk_io_stats()) == type(dict())

def test_net_stats(mocker):
    """
    test function runs and returns dict - 1 bool arg
    """
    mocker.patch('psutil.net_io_counters')
    assert psdata.get_net_stats(True)
    psutil.net_io_counters.assert_called_with(True)
    type(psdata.get_net_stats(True)) == type(dict())

def test_proc_stats(mocker):
    """
    test function runs and returns dict - no args
    """
    mocker.patch('psutil.pids')
    assert psdata.get_proc_stats()
    psutil.pids.assert_called_with()
    type(psdata.get_proc_stats()) == type(dict())
