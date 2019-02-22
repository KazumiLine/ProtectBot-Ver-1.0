# -*- coding: utf-8 -*-
from akad.ttypes import MediaType

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin
    
class LineCall(object):
    isLogin = False
    client  = None

    def __init__(self, client):
        if type(client) is not LineClient:
            raise Exception("You need to set LineClient instance to initialize LineCall")
        self.client = client
        
    def acquireCallRoute(self, to):
        return self.client.call.acquireCallRoute(to)
        
    def acquireGroupCallRoute(self, groupId, mediaType=MediaType.AUDIO):
        return self.client.call.acquireGroupCallRoute(groupId, mediaType)

    def getGroupCall(self, ChatMid):
        return self.client.call.getGroupCall(ChatMid)
        
    def inviteIntoGroupCall(self, chatId, contactIds=[], mediaType=MediaType.AUDIO):
        return self.client.call.inviteIntoGroupCall(chatId, contactIds, mediaType)
        
class Call(object):
    isLogin = False

    def __init__(self):
        self.isLogin = True
        
    @loggedIn
    def acquireCallRoute(self, to):
        return self.call.acquireCallRoute(to)
        
    @loggedIn
    def acquireGroupCallRoute(self, groupId, mediaType=MediaType.AUDIO):
        return self.call.acquireGroupCallRoute(groupId, mediaType)

    @loggedIn
    def getGroupCall(self, ChatMid):
        return self.call.getGroupCall(ChatMid)
        
    @loggedIn
    def inviteIntoGroupCall(self, chatId, contactIds=[], mediaType=MediaType.AUDIO):
        return self.call.inviteIntoGroupCall(chatId, contactIds, mediaType)