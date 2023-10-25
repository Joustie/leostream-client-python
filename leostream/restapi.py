import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os

class LeostreamClient:
  _session = None

  def get_broker(self):
      return self._broker
    
  def set_broker(self, a):
      self._broker = a
 
  broker = property(get_broker, set_broker)

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(LeostreamClient, cls).__new__(cls)
      cls._broker = os.getenv("LEOSTREAM_API_HOSTNAME")
      cls._login = os.getenv("LEOSTREAM_API_USERNAME")
      cls._password= os.getenv("LEOSTREAM_API_PASSWORD")

      URL="https://"+str(cls._broker)+"/rest/v1/session/login"
      PARAMS = {
      'user_login':cls._login,
      'password':cls._password
      }
    
      response = requests.post(url=URL,json=PARAMS, verify=False)

      data = json.loads(response.text)

      sessionID= "Bearer " + data["sid"]
      cls._session = sessionID
    return cls.instance