from bot_classes import *

Amirhosseyn = Moderator('1', 'amirhosseyn', 12345678, 'tabadol', 'amirhosseyn', 'shakery', 'TD')
Alireza = Admin('alireza', 23456789, 'tabadol', 'alireza', 'rahimi', 'SS')
Mojtaba = Moderator('1', 'mojtaba', 45678901, 'tabadol', 'mojtaba', 'rajayi', 'Coach')

moderators_list = [Amirhosseyn, Mojtaba]
members_list = [Amirhosseyn, Alireza, Mojtaba]
Tabadol = Group('Tabadol', Alireza, 34567890, moderators_list, members_list)

print(Amirhosseyn.score)
Amirhosseyn.score_text('Hi amir how are you ?')
print(Amirhosseyn.score)
print(Amirhosseyn.__reduce__())

# del Amirhosseyn
