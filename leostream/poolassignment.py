from .restapi import LeostreamClient
from .webresource import WebResource
import requests

class LeostreamPoolAssignment(WebResource):
    
    resource_type = "pool-assignments"

    def __init__(self, policy_id, id) -> None:
        self._api = LeostreamClient()
        self.resource = "pool-assignments"
        self._id = id
        self._policy_id = policy_id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies/"+ str(self.policy_id) + "/pool-assignments/" + str(self._id)
        print(self._URL)
        self.data = self.get()

    @classmethod
    def list(cls, policy_id):
        '''
        This method will return a list of all resources of the type specified in the url attribute'''

        cls._api = LeostreamClient()
        cls._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': cls._api._session}
        cls._URL="https://"+str(cls._api.broker)+"/rest/v1/policies/" + str(policy_id) + "/" + cls.resource_type
        response = requests.get(url=cls._URL, headers=cls._HEADERS, verify=False)
        data = response.json()

        # check https status code
        if response.status_code != 200:
            raise Exception("Error: the request returned HTTP status code " + str(response.status_code) + " with the following message: " + str(data))

        return data
