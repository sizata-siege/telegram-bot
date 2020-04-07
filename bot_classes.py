from scoring_rules import *


# -----------------------------------------------------------#

class User:
    def __init__(self, username, chatid, groups, firstname, lastname, post):
        self.username = username
        self.chatid = chatid
        self.groups = groups
        self.firstname = firstname
        self.lastname = lastname
        self.post = post
        self.score = 0
        self.nosm = 0
        self.nofm = 0
        self.norm = 0
        self.nosw = 0
        self.nosv = 0

    def __str__(self):
        summery = str(self.username + ' ' + self.groups + ' ' + self.firstname + ' ' + self.lastname)
        return summery

    def add_score(self, score):
        self.score += score

    def score_text(self, text):
        self.nosm += 1
        self.score += text_score + word_score * (text.count(' ') + 1)

    def score_forward(self, text):
        self.nofm += 1
        self.score += forward_score + word_score * (text.count(' ') + 1)

    def score_reply(self, text):
        self.norm += 1
        self.score += reply_score + word_score * (text.count(' ') + 1)


# -----------------------------------------------------------#

class Moderator(User):
    def __init__(self, permission, username, chatid, groups, firstname, lastname, post):
        super().__init__(username, chatid, groups, firstname, lastname, post)
        self.IsModerator = 1
        self.permission = permission


# -----------------------------------------------------------#
class Admin(User):
    def __init__(self, username, chatid, groups, firstname, lastname, post):
        super().__init__(username, chatid, groups, firstname, lastname, post)
        self.IsAdmin = 1


# -----------------------------------------------------------#

class Group:
    def __init__(self, name, admin, chatid, moderators, members):
        self.name = name
        self.owner = admin
        self.chatid = chatid
        self.admins = moderators
        self.members = members


# -----------------------------------------------------------#

class Channel:
    def __init__(self, name, admin, chatid, moderators):
        self.name = name
        self.owner = admin
        self.chatid = chatid
        self.admins = moderators


# -----------------------------------------------------------#
