import pytest
from pyhealthz import web

# Decorator to aid reuse
@pytest.fixture
def parser():
    #Instantiate instance of web function (main entry) arg parser
    return web.create_parser()


# Sad Paths
def test_invalid_arg_failure(parser):
    """
    pyheakthz should exit if invalid arg passed
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--invalid', 'arg'])

def test_invalid_range_tcp_port(parser):
    """
    web argparse exits if TCP port invalid
    ie != 1-65535
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--port', '65536'])

def test_invalid_ipv4_interface_address(parser):
    """
    test parser fails with an invalid ipv4 address
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--address', '256.111.222.333'])

def test_web_server_runs(parser):
    parser.parse_args(['--port', '33333'])

# Happy Paths
def test_default_no_args(parser):
    """
    no args succeeds
    """
    assert parser.parse_args([])

def test_valid_range_tcp_port(parser):
    """
    test a valid tcp port is accepted
    """
    assert parser.parse_args(['--port', '8181'])

def test_valid_ipv4_interface_address(parser):
    """
    test acceptance of properly formed ipv4 address
    """
    assert parser.parse_args(['-a', '127.0.0.1'])
