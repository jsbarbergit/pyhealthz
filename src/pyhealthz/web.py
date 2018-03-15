import ipaddress
import socketserver
import sys
import signal
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from argparse import ArgumentParser, Action, ArgumentTypeError
from pyhealthz import content

#Custom argparse action to validate tcp port given
class PortValidateOption(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        port = int(values[0])
        if port < 1 or port > 65535:
            parser.error(f'Invalid TCP Port Specified. Valid range 1-65535')
        else:
            namespace.port = port

# Web Server Request Handler
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Override server/sys versions to deprive attacker of easy info
        self.server_version = 'pyhealthz'
        self.sys_version = ''
        if self.path == "/healthz":
            #Get dict of all stats
            msg_body = json.dumps(content.get_healthz())
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.flush_headers()
            self.wfile.write(bytes(msg_body, 'utf8'))
        elif self.path == "/":
            msg_body = '<html><head pyhealthz web server></head><body><h1>pyhealthz system resource usage data server</h1><p> call /healthz for stats</body></html>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.flush_headers()
            self.wfile.write(bytes(msg_body, 'utf8'))
        else:
            self.send_error(404, 'Page not found', 'Try a page that exists like /healthz')
        return

#Custom argparse action to validate properly formed ipv4 address given
class AddressValidateOption(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        address = values[0]
        try:
            # Try to cast ip addr given to ipv4 address type
            ipaddress.ip_address(address)
            namespace.address = address
        except:
            parser.error(f'Invalid IPv4 Address')

# Arg Parser
def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--port',
            help=f'Which TCP Port to run the pyhealthz web server',
            required=False,
            metavar=('TCP_PORT'),
            nargs=1,
            default=8080,
            action=PortValidateOption
            )
    parser.add_argument('-a', '--address',
            help=f'Which IPv4 address to bind to',
            required=False,
            metavar=('IPv4_ADDRESS'),
            nargs=1,
            default='0.0.0.0',
            action=AddressValidateOption
            )
    return parser

# Handle SIGINT
def signal_handler(signum, frame):
    print(f'\nReceived Signal: {signum}\nTerminating pyhealthz web server')
    sys.exit(0)

# Run the pyhealthz web server
def run_web_server(address, port):
    server_address = (address, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print(f'Starting pyhealthz server.\nListening on http://{address}:{port}')
    print('Ctrl+C to terminate')
    httpd.serve_forever()

def main():
    # Parse cmd line args
    args = create_parser().parse_args()
    # Set up SIGINT handler
    signal.signal(signal.SIGINT, signal_handler)

    # Run web server
    run_web_server(args.address, args.port)
