import re
strings = u'中国china美国American'
print(strings)
ch_pat = re.compile(u'[\u4e00-\u9fa5]+')
en_pat = re.compile('[a-zA-Z]+')
ch_words = ch_pat.findall(strings)
en_words = en_pat.findall(strings)
print(ch_words)
print(en_words)
