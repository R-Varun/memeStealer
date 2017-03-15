import requests
import json

#sux rn

global token
# your api token here
token = ""

berkeleyPage = "1717731545171536"
gtPage = '1773853552839537'

url = "https://graph.facebook.com/v2.8/"
# where page ID is unique facebook page identifier (in url)

#1717731545171536 ucbmfet
def getCurrentPageContent(pageID):
    if (token == None):
        print("must set token first!")
    param = {"access_token": token}
    r = requests.get(url + pageID + "/feed", params=param)
    response = r.json()
    if "error" in response:
        print("An error has occured!")
        print(response["error"]["message"])
        return None
    return response

def getPictureURL(nodeID):
    param = {"fields" : "full_picture", "access_token": token}
    r = requests.get(url + nodeID, params=param)
    if "full_picture" in r.json():
        return r.json()["full_picture"]
    else:
        return None


def stealFirstPost(pageID, giveCredit = False):
    page = getCurrentPageContent(pageID)
    if page == None:
        print("Error")
        return
    dataArr = page["data"]
    firstPost = dataArr[0]
    id = None
    message = None
    if "id" in firstPost:
        id = firstPost["id"]
    if "message" in firstPost:
        message = firstPost["message"]

    if not giveCredit:
        message.replace(" cal ", " gt ")
        message.replace(" Cal ", " GT ")
    else:
        # for no message content
        if message == None:
            message = ""

        message += "\n \n --This meme was stolen from UCBMET"

    picture = getPictureURL(id)
    if picture == None:
        #no picture in post
        print("no picture")
    return {"message" : message, "picture": picture}


def postOnPage(pageID, content):
    if content == None:
        return
    message = content["message"]
    picture = content["picture"]

    # picture post
    if picture != None:
        #post image

        #empty caption
        if message == None:
            message = ""

        pic_payload = {"url": picture, "access_token": token, "caption":message}
        r = requests.post(url + pageID + "/photos", data=pic_payload)
        print(r.json())

    #mesage only
    else:
        payload = {"message":message,"access_token": token}
        r = requests.post(url + pageID + "/feed", data=payload)

    print("done.")

def stealNthPost(pageID, n, giveCredit = False):
    page = getCurrentPageContent(pageID)
    if page == None:
        print("Error")
        return
    dataArr = page["data"]
    firstPost = dataArr[n]
    id = None
    message = None
    if "id" in firstPost:
        id = firstPost["id"]
    if "message" in firstPost:
        message = firstPost["message"]

    if not giveCredit:
        message.replace(" cal ", " gt ")
        message.replace(" Cal ", " GT ")
    else:
        # for no message content
        if message == None:
            message = ""
        message += "\n \n --This meme was stolen from UCBMET"
    picture = getPictureURL(id)
    if picture == None:
        #no picture in post
        print("no picture")
    return {"message" : message, "picture": picture}

#usage
#postOnPage(gtPage, stealFirstPost(berkeleyPage, True))




