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

def test_psutil_result_parser_returns_list():
    """
    psutil parsing function should return a list
    even when passed an empty string
    """
    assert dict(psdata.psutil_result_parser('scputimes(user=2.0, nice=0.0, system=1.2, idle=96.8)', 'test_metric'))
    assert psdata.psutil_result_parser('','') == {}
