import unittest
import requests
import json

from utils import USERS

Host = "http://127.0.0.1:5000"


class TestStringMethods(unittest.TestCase):

    def test_read_atm(self):
        res = requests.get(Host+"/api/get_atm/1", auth=(USERS[0]["username"], USERS[0]["passwd"]))
        assert res.status_code is 200
        res = res.json()
        assert "address" in res.keys()
        assert "uid" in res.keys()
    
    def test_add_atm(self):
        data = {"address":{"street":"kbhp","housenumber":"84","postalcode":"50082 DN","city":"Hyd","geoLocation":{"lat":"52.246215","lng":"4.82709"}},"distance":0,"openingHours":[{"dayOfWeek":2,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":3,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":4,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":5,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":6,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":7,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":1,"hours":[{"hourFrom":"10:00","hourTo":"19:00"}]}],"functionality":"Geldautomaat","type":"GELDMAAT"}
	
        res = requests.post(Host+"/api/add_atm", data = json.dumps(data), headers={'Content-type': 'application/json'}, auth=(USERS[0]["username"], USERS[0]["passwd"]))
        
        assert res.status_code is 201
        
        assert "ATM added successfully" in res.text
        
    def test_update_atm(self):
        data = {"uid":1,"address":{"street":"kbhp","housenumber":"84","postalcode":"50082 DN","city":"Hyd","geoLocation":{"lat":"52.246215","lng":"4.82709"}},"distance":0,"openingHours":[{"dayOfWeek":2,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":3,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":4,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":5,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":6,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":7,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":1,"hours":[{"hourFrom":"10:00","hourTo":"19:00"}]}],"functionality":"Geldautomaat","type":"GELDMAAT"}
	
        res = requests.put(Host+"/api/update_atm", data = json.dumps(data), headers={'Content-type': 'application/json'}, auth=(USERS[0]["username"], USERS[0]["passwd"]))
        #print(res.text)
        assert res.status_code is 200
        
        assert "ATM Info Updated" in res.text

    def test_delete_atm(self):
        #data = {"uid":1,"address":{"street":"kbhp","housenumber":"84","postalcode":"50082 DN","city":"Hyd","geoLocation":{"lat":"52.246215","lng":"4.82709"}},"distance":0,"openingHours":[{"dayOfWeek":2,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":3,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":4,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":5,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":6,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":7,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":1,"hours":[{"hourFrom":"10:00","hourTo":"19:00"}]}],"functionality":"Geldautomaat","type":"GELDMAAT"}
	
        res = requests.delete(Host+"/api/delete_atm/2", auth=(USERS[0]["username"], USERS[0]["passwd"]))
        #print(res.text)
        assert res.status_code is 200
        
        assert "ATM deleted successfully" in res.text


if __name__ == '__main__':
    unittest.main()
    