import logging,requests

def search_query_by_filter(api_key, filter):
    try:
        response = requests.get(
            url="https://api.todoist.com/rest/v2/tasks",
            params={
                "filter": filter,
            },
            headers={
                "Authorization": "Bearer " + api_key,
            },
        )
        if response.status_code == 200:
            return response.json()
        else:
            logging.warn("Status: %d, result: %s", response.status_code, response.json())
            return None
    except requests.exceptions.RequestException as e:
        logging.error(e)
        return None
