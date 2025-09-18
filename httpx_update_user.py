from tools.fakers import fake
import httpx


url = "http://127.0.0.1:8000"
def create_user():
    end_point = url + "/api/v1/users"
    payload = {
        "email": fake.email(),
        "password": "12345",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    resp = httpx.post(end_point, json=payload)
    print(resp.status_code)
    return resp.json()['user']['id'], payload

def authentication_to_system(user_info):
    end_point = url + "/api/v1/authentication/login"
    payload = {
        "email": user_info['email'],
        "password": user_info['password']
    }
    resp = httpx.post(end_point, json=payload)
    print(resp.status_code)
    return resp.json()["token"]["accessToken"]

def patch_user(user_id, token):
    end_point = url + f"/api/v1/users/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "email": fake.email(),
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    resp = httpx.patch(end_point, headers=headers, json=payload)
    print(resp.status_code)


if __name__ == "__main__":
    user_id, create_payload = create_user()
    token = authentication_to_system(create_payload)
    patch_user(user_id, token)
