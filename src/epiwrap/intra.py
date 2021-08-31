import requests as r
import datetime

class EpiError(Exception):
    def __init__(self, err):
        self.message = err
        self.value = "EpiError Error : " + self.message

    def __str__(self):
        return repr(self.value)


class Module(object):
    def __init__(self, ew, module, code, year=datetime.datetime.now().year):
        self.title = ""
        self.end_register = ""
        self.end = ""
        self.credit = ""
        self.student_grade = ""
        self.activites = []
        res = r.get(
            ew.get_url() + "/module/" + str(year) + "/" + module + "/" + code + "/?format=json",
            headers=ew.get_header(),
            cookies=ew.get_token()
        )
        if res.status_code == 403:
            raise EpiError("Bad token/Not connected")
        res = res.json()
        for i in res:
            self.__setattr__(i, res[i])



class Student(object):
    """Student class"""
    def __init__(self, ew):
        try:
            res = r.get(
                ew.get_url() + "/user/?format=json",
                         headers=ew.get_header(),
                         cookies=ew.get_token()
                        )
            if res.status_code == 403:
                raise EpiError("Bad token/Not connected")
            res = res.json()
            for i in res:
                self.__setattr__(i, res[i])
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

    def get_module(self, module, code):
        mod = Module(self, module, code)
        return mod