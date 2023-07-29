import logging,os,sys,time,yaml
from prometheus_client import CollectorRegistry, Gauge, start_http_server
import modules.todoist as td

log_format = '%(asctime)s[%(filename)s:%(lineno)d][%(levelname)s] %(message)s'
logging.basicConfig(format=log_format, datefmt='%Y-%m-%d %H:%M:%S%z', level=logging.INFO)

if __name__ == '__main__':

    api_key = os.environ.get('TODOIST_API_KEY')
    if api_key == None:
        logging.fatal("Can't get Todoist API Key. Please set 'TODOIST_API_KEY' environment!")
        sys.exit(1)

    logging.info("initializing exporter...")
    registry = CollectorRegistry()
    start_http_server(int(os.environ.get('PORT', 8000)), registry=registry)

    logging.info("create all metrics instances...")
    g = Gauge('todoist_filter_task_items','todoist item\'s amount by unique filter', ['name', 'filter'], registry=registry)

    logging.info("loading config file...")
    with open('config.yml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    
    while True:
        logging.info("start fetch filter nums...")
        for filter in config['filters']:
            logging.info("Fetching tasks by filter: %s", filter['query'])
            result = td.search_query_by_filter(api_key, filter['query'])

            if result == None:
                logging.error("Failed to fetch result: %s", filter['query'])
            else:
                logging.debug("Fetched result: %s", result)
                logging.info("Fetching tasks Successful: %s", filter['query'])
                g.labels(filter['name'], filter['query']).set(len(result))
        time.sleep(300)
