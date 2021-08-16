import requests as r


class EpiError(Exception):
    def __init__(self, err):
        self.message = err
        self.value = "EpiError Error : " + self.message

    def __str__(self):
        return repr(self.value)


class Student(object):
    """coucou"""
    def __init__(self, token, header):
        try:
            res = r.get("https://intra.epitech.eu/user/?format=json", headers=header, cookies=token).json()
            self.fullname = res["title"]
            self.gpa = res["gpa"][0]["gpa"]
            self.firstname = res["firstname"]
            self.lastname = res["lastname"]
            self.city = res["groups"][0]["title"]
            self.credits = res["credits"]
            self.scolaryear = res["promo"]
            self.semester = res["semester"]
        except Exception as e:
            print(e)


class EpiWrap(object):
    """Simple local wrapper for epitech intra"""

    def __init__(self, token):
        """Enter token in parameters to initiate the client"""
        self._done = False
        self._url = ""
        self._types = {"GET": r.get,
                       "POST": r.post,
                       "DELETE": r.delete}
        self._method = ""
        self._data = "bytearray(json.dumps(data), 'utf8')"
        self._error = None
        self._request = None
        self._token = {"user": token}
        self._headers = {"Content-Type": "application/json", "Accept-Language": "fr,en-US;q=0.8,en;q=0.6"}

    def getToken(self):
        return self._token

    def getHeader(self):
        return self._headers

    def getProfile(self):
        try:
            student = Student(self.getToken(), self.getHeader())
            return student
        except EpiError as e:
            print(e)
