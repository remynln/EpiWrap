from flask import Blueprint, request
import json
from time import strftime
from datetime import timedelta, date, datetime
from src import formater as f


class URLArgError(Exception):

    def __init__(self, value):
        self.message = value
        self.value = "URLArg Error : " + self.message

    def __str__(self):
        return repr(self.value)


def getArg(key, default=None):
    args = request.args.get(key)
    head = request.headers.get(key)
    if not args and not head:
        if default is not None:
            return default
        else:
            raise URLArgError("Missing argument {0}".format(key))
    return args if args else head


def checkAuth(req):
    if not req:
        return f.error("Missing token", 401)
    result = f.executeRequest(req)
    if result["code"] == 200:
        return f.response(result["data"], 200)
    if "message" in result["data"]:
        return f.error(result["data"]["message"], 401)
    elif "error" in result["data"]:
        return f.error(result["data"]["error"], 401)
    else:
        return f.error("There is an error, try again", 401)


def getTokenRequest(url, method, data=None):
    req = f.Request(url, method, data)
    try:
        req.setCookie("user", getArg("token"))
        return req
    except URLArgError:
        return None


def get_route(route):
    return "https://intra.epitech.eu" + route


def root():
    return f.response({"status": True}, 200)


def getInfos():
    req = getTokenRequest(get_route("/?format=json"), "GET")
    return checkAuth(req)


def getPlanning():
    try:
        start = getArg("start", strftime("%Y-%m-%d", date.today().timetuple()))
        end = getArg("end", (datetime.strptime(start, "%Y-%m-%d") + timedelta(days=6)))
        route = "/intra/planning/load?format=json&start={0}&end={1}".format(start, str(end).split(' ')[0])
    except URLArgError as e:
        return f.error(e.message, 401)
    req = getTokenRequest(get_route(route), "POST")
    return checkAuth(req)
