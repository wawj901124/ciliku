# pip install translate
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple translate


from translate import Translator


# 以下是将简单句子从英语翻译中文
translator= Translator(to_lang="chinese")
translation = translator.translate("Good night!")
print(translation)


# 在任何两种语言之间，中文翻译成英文
translator= Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("我想你")
print(translation)

mylist = ['网页', '类别', '片名', '女优', '大小', '步骑', '时间', '磁力', '预览', '预览', '预览']

my_english_list = []
for one in mylist:
    translator = Translator(from_lang="chinese", to_lang="english")
    translation = translator.translate(one)
    my_english_list.append(translation.replace(" ", "_").lower())  #空格替换成下划线

print(mylist)
print(my_english_list)

mylist_len = len(mylist)
for i in range(0,mylist_len):
    one = """
    %s = models.CharField(max_length=100, default="", verbose_name=u"%s")""" %(my_english_list[i],mylist[i])
    print(one)
