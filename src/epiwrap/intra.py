import requests as r

class EpiError(Exception):
    def __init__(self, err):
        self.message = err
        self.value = "EpiError Error : " + self.message

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return str(self)

class Student(object):
    """Student class"""
    def __init__(self, epiwrap):
        try:
            res = r.get(
                epiwrap.get_url() + "/user/?format=json",
                         headers=epiwrap.get_header(),
                         cookies=epiwrap.get_token()
                        )
            if res.status_code == 403:
                raise EpiError("Bad token/Not connected")
            res = res.json()
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

    def __init__(self, token="", autolog="https://intra.epitech.eu"):
        """Enter token in parameters to initiate the client"""
        self._done = False
        self._url = autolog
        self._types = {"GET": r.get,
                       "POST": r.post,
                       "DELETE": r.delete}
        self._method = ""
        self._data = "bytearray(json.dumps(data), 'utf8')"
        self._error = None
        self._request = None
        self._token = {"user": token}
        self._headers = {"Content-Type": "application/json", "Accept-Language": "fr,en-US;q=0.8,en;q=0.6"}

    def get_token(self):
        return self._token

    def get_url(self):
        return self._url

    def get_header(self):
        return self._headers

    def get_profile(self):
        try:
            student = Student(self)
            return student
        except EpiError as e:
            print(e)
