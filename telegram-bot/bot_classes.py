from scoring_rules import *


# users must be initialized first and then be added to groups as members
# users must be declared by their chat_id not username so if a user has no username there is no bugs and NoUsername will be replaced by username
# prices must be monthly or 3 months or 6 or more and must be based on group size and the number of members of the groups for example less than 20 or between 20,50 or between 50,250 or 250,1000 or 1000,5000 or 5000,25000 or 25000,100000 or more on
# Add Language select option
# admin should see the activities and projects users sent and should score them using options under each message ( activity / project )
# user can see his sent activities and projects and how much score have those got from moderator or admin
# ----------------------------------------------------------- #

class User:
    def __init__(self, chat_id, username, groups, first_name, last_name, post):
        self.chat_id = chat_id
        self.username = username
        self.groups = []
        self.groups = groups
        self.first_name = first_name
        self.last_name = last_name
        self.post = post
        self.score = 0
        self.nosm = 0
        self.nofm = 0
        self.norm = 0
        self.nosw = 0
        self.nosv = 0
        self.nosa = 0
        self.nosp = 0

    def __str__(self):
        summery = str(
            self.username + ' | ' + self.groups + ' | ' + self.first_name + ' | ' + self.last_name + ' | ' + self.chat_id)
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

    def reset_score(self):
        self.score = 0
        self.nosm = 0
        self.nofm = 0
        self.norm = 0
        self.nosw = 0
        self.nosv = 0

    def add_group(self, group_name, chat_id=None):
        self.groups.append(group_name)

    def get_detailed_stats(self):
        return self.score, self.nosm, self.nofm, self.norm, self.nosw, self.nosv

    def get_score(self):
        return self.score  # better to use user.score instead of this function I think

    # ----------------------------------------------------------- #


class Moderator(User):
    def __init__(self, permission, chat_id, username, groups, first_name, last_name, post):
        super().__init__(chat_id, username, groups, first_name, last_name, post)
        self.IsModerator = 1
        self.permission = permission


# ----------------------------------------------------------- #
class Admin(User):  # change to owner
    def __init__(self, chat_id, username, groups, first_name, last_name, post):
        super().__init__(chat_id, username, groups, first_name, last_name, post)
        self.IsAdmin = 1

    def get_group_stats(self, group):
        pass  # all user stats


# ----------------------------------------------------------- #

class Group:
    def __init__(self, name, admin, chat_id, moderators, members=None):
        self.name = name
        self.owner = admin
        self.chat_id = chat_id
        self.admins = moderators
        self.members = []
        if members:
            self.members = members

    def __str__(self):
        pass

    def reset_users_scores(self):  # or reset_group_scores(self):  # or both
        pass

    def add_user(self, user):
        self.members.append(user)


# ----------------------------------------------------------- #

class Channel:
    def __init__(self, name, admin, chat_id, moderators):
        self.name = name
        self.owner = admin
        self.chat_id = chat_id
        self.admins = moderators

# ----------------------------------------------------------- #
