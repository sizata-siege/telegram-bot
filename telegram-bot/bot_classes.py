from scoring_rules import *
import database as db

# users must be initialized first and then be added to groups as members
# users must be declared by their chat_id not username so if a user has no username there is no bugs and NoUsername will be replaced by username
# prices must be monthly or 3 months or 6 or more and must be based on group size and the number of members of the groups for example less than 20 or between 20,50 or between 50,250 or 250,1000 or 1000,5000 or 5000,25000 or 25000,100000 or more on
# Add Language select option
# admin should see the activities and projects users sent and should score them using options under each message ( activity / project )
# user can see his sent activities and projects and how much score have those got from moderator or admin
# create an installer that downloads all the files and scripts from the server and
# places them in their certain directories and configures them

sq = db.sqlite
my = db.mysql

# ----------------------------------------------------------- #
class Plan:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ' : ' + str(self.price)


plan_trial = Plan('trial', 0)
plan_premium = Plan('premium', 15000)

# ----------------------------------------------------------- #


class User:
    def __init__(self, chat_id: int, username: str, first_name: str, last_name: str):  # , **kwargs, groups: list, post: str
        self.chat_id = chat_id
        self.username = username
        self.groups = []
        # self.groups = groups
        self.first_name = first_name
        self.last_name = last_name
        # self.post = post
        self.score = 0
        self.smc = 0  # sent messages count
        self.fmc = 0
        self.rmc = 0
        self.swc = 0
        self.svc = 0
        self.sac = 0
        self.spc = 0

    def __str__(self):
        summery = str(
            self.username + ' | ' + str(self.groups) + ' | ' + self.first_name + ' | ' + self.last_name + ' | ' + str(self.chat_id))
        return summery

    def add_score(self, score: int):
        self.score += score

    def score_text(self, text: str):
        self.smc += 1
        self.score += text_score + word_score * (text.count(' ') + 1)

    def score_forward(self, text: str):
        self.fmc += 1
        self.score += forward_score + word_score * (text.count(' ') + 1)

    def score_reply(self, text: str):
        self.rmc += 1
        self.score += reply_score + word_score * (text.count(' ') + 1)

    def reset_score(self):
        self.score = 0
        self.smc = 0
        self.fmc = 0
        self.rmc = 0
        self.swc = 0
        self.svc = 0

    def add_group(self, group_name: str, chat_id=None):
        if chat_id:
            self.groups.append(chat_id)
        else:
            self.groups.append(group_name)

    def get_detailed_stats(self):
        return self.score, self.smc, self.fmc, self.rmc, self.swc, self.svc

    def get_score(self):
        return self.score  # better to use user.score instead of this function I think

    def is_registered(self):
        res = 0
        if sq.check_chat_id(self.chat_id):
            res += 1
        if my.check_chat_id(self.chat_id):
            res += 2
        # if mo.check_chat_id(self.chat_id):
        #     res += 4
        return res  # 0 means no matches | 1 means matches in sqlite db | 2 means matches in mysql db |
        # 3 means matches in both sqlite and mysql | 4 means just in mongo | 5 means ...

    def is_owner(self):
        res = 0
        if sq.is_owner(self.chat_id):
            res += 1
        if my.is_owner(self.chat_id):
            res += 2
        return res

    def is_group_owner(self):
        res = 0
        if sq.is_group_owner(self.chat_id, self.groups[0]):
            res += 1
        if my.is_group_owner(self.chat_id, self.groups[0]):
            res += 2
        return res

    def is_assistant(self):
        res = 0
        if sq.is_assistant(self.chat_id):
            res += 1
        if my.is_assistant(self.chat_id):
            res += 2
        return res

    def is_group_assistant(self):
        res = 0
        if sq.is_group_assistant(self.chat_id, self.groups[0]):
            res += 1
        if my.is_group_assistant(self.chat_id, self.groups[0]):
            res += 2
        return res

# ----------------------------------------------------------- #


class Assistant(User):
    def __init__(self, permission, chat_id, username, first_name, last_name):
        super().__init__(chat_id, username, first_name, last_name)
        self.IsAssistant = 1
        self.permission = permission


# ----------------------------------------------------------- #
class Owner(User):  # change to owner show as manager in the bot
    def __init__(self, chat_id, username, first_name, last_name):
        super().__init__(chat_id, username, first_name, last_name)
        self.IsOwner = 1

    def get_group_stats(self, group):
        pass  # all user stats


# ----------------------------------------------------------- #

class Group:
    def __init__(self, name: str, owner: Owner, chat_id: int, managers: Assistant, members=None, scoring_rules=None, plan: Plan = plan_trial):  # use telegram classes instead of my own classes. How ???
        self.name = name
        self.owner = owner
        self.chat_id = chat_id
        self.plan = plan
        self.managers = managers
        self.members = []
        if members:
            self.members = members
        if scoring_rules:
            self.scoring_rules = scoring_rules
        else:
            # global default_scoring_rules
            self.scoring_rules = default_scoring_rules

    def __str__(self):
        pass

    def reset_users_scores(self):  # or reset_group_scores(self):  # or both
        pass

    def add_user(self, user):
        self.members.append(user)

    def is_registered(self):
        res = 0
        if sq.check_group_chat_id(self.chat_id):
            res += 1
        if my.check_group_chat_id(self.chat_id):
            res += 2
        return res


# ----------------------------------------------------------- #

class Channel:
    def __init__(self, name, admin, chat_id, moderators):
        self.name = name
        self.owner = admin
        self.chat_id = chat_id
        self.admins = moderators

# ----------------------------------------------------------- #
