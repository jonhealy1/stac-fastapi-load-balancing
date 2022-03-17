from locust import HttpUser, task, between
import random
import json

class WebsiteTestUser(HttpUser):

    # wait_time = between(0.0001, 0.0002)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    def load_file(self, file) -> dict:
        f = open(file)
        data = json.load(f)
        return data

    @task(1)
    def get_root_catalog(self):
        self.client.get("http://localhost:8083")

    @task(2)
    def get_all_collections(self):
        self.client.get("http://localhost:8083/collections")

    @task(3)
    def get_collection(self):
        self.client.get("http://localhost:8083/collections/test-collection")

    @task(4)
    def get_item_collection(self):
        self.client.get("http://localhost:8083/collections/test-collection/items")

    @task(5)
    def get_item(self):
        random_number = random.randint(1, 11)
        item = self.load_file('data_loader/setup_data/sentinel-s2-l2a-cogs_0_100.json')
        random_id = item["features"][random_number]["id"]
        self.client.get(f"http://localhost:8083/collections/test-collection/items/{random_id}")

    @task(6)
    def get_bbox_search(self):
        self.client.get("http://localhost:8083/search?bbox=-16.171875,-79.095963,179.992188,19.824820")

    # @task(7)
    # def post_bbox_search(self):
    #     self.client.post("http://localhost:8083/search", json={"bbox":[16.171875,-79.095963,179.992188,19.824820]})

    @task(8)
    def post_bbox_search(self):
        self.client.post("http://localhost:8083/search", json={"bbox":[16.171875,-79.095963,179.992188,19.824820]})
        self.client.post(
            "http://localhost:8083/search", 
            json={
                "collections":["test-collection"],
                "intersects":{"type": "Point", "coordinates": [150.04, -33.14]}
            }
        )
