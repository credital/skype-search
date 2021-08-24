import requests, random

class Skype:
    def __init__(self, token):
        self.skype_token = token
        self.session = requests.session()
        self.session.headers.update({"X-Skypetoken": self.skype_token, "X-ECS-ETag": "", "X-Skype-Client": "", "X-SkypeGraphServiceSettings": ""})

    def search(self, search_query):
        params = {
            "searchString": search_query,
            "requestId": random.randint(1e13, 9e13)
        }

        search_response = self.session.get("https://skypegraph.skype.com/v2.0/search", params = params)

        if search_response.status_code == 200:
            json_response = search_response.json()
            relevant_data = json_response["results"]
            output = []

            for info in relevant_data:
                output.append(info["nodeProfileData"])

            return output

if __name__ == "__main__":
    skype_token = open("../auth/token", "r").readline().strip()

    client = Skype(skype_token)

    while True:
        search_query = input("Search Query: ").strip().lower()
        search_response = client.search(search_query)
        
        print(search_response)


