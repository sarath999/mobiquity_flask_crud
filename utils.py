

ATMS = [{"uid": 1, "address":{"street":"Zijdelwaardplein","housenumber":"84","postalcode":"1422 DN","city":"Uithoorn","geoLocation":{"lat":"52.246215","lng":"4.82709"}},"distance":0,"openingHours":[{"dayOfWeek":2,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":3,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":4,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":5,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":6,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":7,"hours":[{"hourFrom":"08:00","hourTo":"22:00"}]},{"dayOfWeek":1,"hours":[{"hourFrom":"10:00","hourTo":"19:00"}]}],"functionality":"Geldautomaat","type":"GELDMAAT"}]

USERS = [{"username":"sarat", "passwd":"bobba"}, {"username":"ree", "passwd":"oct"}]

def user_validator(uname, passwd):
    cred = {"username": uname, "passwd": passwd}
    if cred in USERS:
        return True
    else:
        return False


def get_atm_by_uid(uid): 
    return next((item for item in ATMS if item["uid"] == int(uid)), None)

def get_atm_by_addr(data): 
    return next((item for item in ATMS if item["address"] == data), None)