text_score = 30
word_score = 1
forward_score = 35
reply_score = 40
voice_score = 50
voice_score_per_second = 0.5
voice_score_per_minute = voice_score_per_second * 60
link_score = 20

default_scoring_rules = {
    'text': 30,
    'word': 1,
    'forward': 35,
    'reply': 40,
    'voice': 50,
    'voice_per_second': 0.5,
    'voice_per_minute': voice_score_per_second * 60,
    'link': 20
}


# and other rules

# saving the data in a json file or something else

def set_text_score(score):
    global text_score
    text_score = score
    default_scoring_rules['text'] = score


def set_word_score(score):
    global word_score
    word_score = score
    default_scoring_rules['word'] = score


def set_forward_score(score):
    global forward_score
    forward_score = score
    default_scoring_rules['forward'] = score


def set_reply_score(score):
    global reply_score
    reply_score = score
    default_scoring_rules['reply'] = score


def set_voice_score(score):
    global voice_score
    voice_score = score
    default_scoring_rules['voice'] = score


def set_voice_score_per_second(score):
    global voice_score_per_second
    voice_score_per_second = score
    default_scoring_rules['voice_per_second'] = score


def set_voice_score_per_minute(score):
    global voice_score_per_minute
    voice_score_per_minute = score
    default_scoring_rules['voice_per_minute'] = score


def set_link_score(score):
    global link_score
    link_score = score
    default_scoring_rules['link'] = score


# print(scores['text'])
# set_text_score(32)
# print(scores['text'])
