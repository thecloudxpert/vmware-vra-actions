def create_group (gName);
    api_url = '{0}/policy/api/v1/infra/domains/default/groups/{1}'.format(api_url,gName)
    payload = {
             "description": gName,
            "display_name": gName
    }
    headers = {
        "Authorization": 
        "Content-Type": 'application/json'
    }
    response = requests