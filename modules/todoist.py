import requests

def search_query_by_filter(api_key, filter):
    # Request
    # GET https://api.todoist.com/rest/v1/tasks

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
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
