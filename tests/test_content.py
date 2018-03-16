import pytest
from pyhealthz import content, psdata

# Happy Paths

def test_get_cpu_stats(mocker):
    """
    Returns dict of cpu stats
    """
    # Mock the psdata calls as otherwise this is an int test
    mocker.patch('pyhealthz.psdata.get_single_cpu_pct_all_states')
    assert content.get_cpu_stats()
    type(content.get_cpu_stats()) == type(dict())

def test_get_health(mocker):
    """
    Returns a dictionary
    """
    mocker.patch('pyhealthz.psdata.get_single_cpu_pct_all_states')
    assert content.get_healthz()
    assert type(content.get_healthz()) == type(dict())

def test_get_virtualmemory_stats(mocker):
    """
    Returns dict of virtual memory stats
    """
    # Mock the psdata calls as otherwise this is an int test
    mocker.patch('pyhealthz.psdata.get_virtual_memory_stats')
    assert content.get_virtualmemory_stats()
    type(content.get_virtualmemory_stats() ) == type(dict())

def test_get_disk_usage_stats(mocker):
    """
    Returns dict of disk usage stats
    """
    mocker.patch('pyhealthz.psdata.get_disk_usage_stats')
    assert content.get_disk_usage_stats()
    type(content.get_disk_usage_stats() ) == type(dict())

def test_get_disk_partitions(mocker):
    """
    Returns dict of disk partitions
    """
    mocker.patch('pyhealthz.psdata.get_disk_partitions')
    assert content.get_disk_partition_stats()
    type(content.get_disk_partition_stats() ) == type(dict())

def test_get_disk_io(mocker):
    """
    Returns dict of disk io counters
    """
    mocker.patch('pyhealthz.psdata.get_disk_io_stats')
    assert content.get_disk_io_stats()
    type(content.get_disk_io_stats() ) == type(dict())

def test_get_net_stats(mocker):
    """
    returns a dict of net io counters
    """
    mocker.patch('pyhealthz.psdata.get_net_stats')
    assert content.get_net_stats()
    type(content.get_net_stats() ) == type(dict())

def test_get_proc_stats(mocker):
    """
    returns a dict of process stats
    """
    mocker.patch('pyhealthz.psdata.get_proc_stats')
    assert content.get_proc_stats()
    type(content.get_proc_stats() ) == type(dict())
