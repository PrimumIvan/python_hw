import requests


class ProjectApi:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create(self, payload: dict, with_auth: bool = True):
        """[POST] /api-v2/projects — создание проекта."""
        headers = (
            self.headers
            if with_auth
            else {"Content-Type": "application/json"}
        )
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=headers,
            timeout=15,
        )

    def update(self, project_id: str, payload: dict, with_auth: bool = True):
        """[PUT] /api-v2/projects/{id} — изменение проекта."""
        headers = (
            self.headers
            if with_auth
            else {"Content-Type": "application/json"}
        )
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=headers,
            timeout=15,
        )

    def get_by_id(self, project_id: str, with_auth: bool = True):
        """[GET] /api-v2/projects/{id} — получение проекта по ID."""
        headers = (
            self.headers
            if with_auth
            else {"Content-Type": "application/json"}
        )
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=headers,
            timeout=15,
        )
