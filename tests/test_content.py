import pytest
from pyhealthz import content, psdata

# Happy Paths

def test_get_cpu_stats(mocker):
    """
    Returns list of cpu stats
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
