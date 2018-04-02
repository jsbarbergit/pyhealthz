from prometheus_client import start_http_server, Metric, REGISTRY
import json
import requests
import sys
import time

class JsonCollector(object):
  def __init__(self, endpoint):
    self._endpoint = endpoint
  def collect(self):
    # Fetch the JSON
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))

    # Convert requests and duration to a summary in seconds
    metric = Metric('pyhealthz_cpu_stats',
        'Pyhealthz CPU stats', 'summary')
    metric.add_sample('pyhealthz_cpu_user_pct',
        value=float(response['cpu_total']['user']), labels={})
    metric.add_sample('pyhealthz_cpu_idle_pct',
        value=float(response['cpu_total']['idle']), labels={})
    yield metric

if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2]))

  while True: time.sleep(1)
