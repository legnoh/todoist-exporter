import yaml
import time
import os
from prometheus_client import CollectorRegistry, Gauge, start_http_server
import modules.todoist as td

def export_filter_nums(filters, api, gauge):
    for filter in filters:
        result = td.search_query_by_filter(api_key, filter['query'])
        g.labels(filter['name'], filter['query']).set(len(result))

if __name__ == '__main__':
    registry = CollectorRegistry()
    start_http_server(int(os.environ['PORT']), registry=registry)

    g = Gauge('todoist_filter_task_items','todoist item\'s amount by unique filter', ['name', 'filter'], registry=registry)

    with open('config.yml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    
    api_key = os.environ['TODOIST_API_KEY']
    
    while True:
        export_filter_nums(config['filters'], api_key, g)
        time.sleep(300)
