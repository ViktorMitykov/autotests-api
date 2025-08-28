import httpx

url = "http://127.0.0.1:8000"
def get_access_token():
    end_point = url + "/api/v1/authentication/login"
    body = {
        "email": "user@example.com",
        "password": "string"
    }

    resp = httpx.post(end_point, json=body)
    access_token = resp.json()["token"]["accessToken"]
    return access_token

def get_user_info():
    end_point = url + "/api/v1/users/me"
    acces_token = get_access_token()
    headers = {"Authorization": f"Bearer {acces_token}"}

    resp = httpx.get(end_point, headers=headers)
    print(resp.json())

if __name__=="__main__":
    get_user_info()