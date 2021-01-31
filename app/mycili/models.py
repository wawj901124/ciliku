from datetime import datetime   #系统的包放在最上面

from django.db import models   #第二个级别的就是第三方包
from django.contrib.auth import  get_user_model  #导入get_user_model

from ciliku.settings import DJANGO_SERVER_YUMING

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


#Create your models here.
class videoCiLi(models.Model):#继承django的Model模块
    """
    磁力库
    """
    web = models.CharField(max_length=100, default="", verbose_name=u"网页")

    category = models.CharField(max_length=100, default="", verbose_name=u"类别")

    original_title = models.CharField(max_length=100, default="", verbose_name=u"片名")

    actress = models.CharField(max_length=100, default="", verbose_name=u"女优")

    size = models.CharField(max_length=100, default="", verbose_name=u"大小")

    step_riding = models.CharField(max_length=100, default="", verbose_name=u"步骑")

    time = models.CharField(max_length=100, default="", verbose_name=u"时间")

    magnetic_force = models.CharField(max_length=1500, default="", verbose_name=u"磁力")

    preview_one = models.CharField(max_length=1500, default="", verbose_name=u"预览1")

    preview_two = models.CharField(max_length=1500, default="", verbose_name=u"预览2")

    preview_three = models.CharField(max_length=1500, default="", verbose_name=u"预览3")



    # test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    # test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    # test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    # case_priority = models.CharField(max_length=10,null=True, blank=True,
    #                                  choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
    #                                  default="P1",
    #                                  verbose_name=u"用例优先级")
    # test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    # is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    #
    # login_url = models.CharField(max_length=1000, default="",null=True, blank=True,
    #                                                      verbose_name=u"登录页的url")
    #
    # is_auto_input_code = models.BooleanField(default=False,verbose_name=u"是否自动输入验证码")
    #
    # code_image_xpath = models.CharField(max_length=1000, default="",null=True, blank=True,
    #                                                      verbose_name=u"验证码xpath路径")
    #
    # code_type = models.CharField(max_length=10, default="n4",null=True, blank=True,verbose_name=u"验证码类型",
    #                              help_text=u"验证码类型：n4(4位纯数字)、n5(5位纯数字)、n6（6位纯数字）、"
    #                                        u"e4（4位纯英文）、e5（5位纯英文）、e6（6位纯英文）、"
    #                                        u"ne4（4位英文数字）、ne5（5位英文数字）、ne6（6位英文数字)" )
    #
    # code_input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
    #                                     verbose_name=u"验证码输入框查找风格",
    #                                     help_text=u"元素查找风格：id、name、class_name、tag_name、"
    #                                               u"link_text、partial_link_text、css_selector、xpath")
    # code_input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
    #                                                      verbose_name=u"验证码输入框查找风格的确切值")
    #
    # login_button_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
    #                                     verbose_name=u"登录按钮查找风格",
    #                                     help_text=u"元素查找风格：id、name、class_name、tag_name、"
    #                                               u"link_text、partial_link_text、css_selector、xpath")
    # login_button_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
    #                                                      verbose_name=u"登录按钮查找风格的确切值")
    # click_login_button_delay_time = models.CharField(max_length=100, default="3", null=True, blank=True,
    #                                             verbose_name=u"点击登录按钮后的延时时长（单位秒）",
    #                                             help_text=u"点击登录按钮后的延时时长（单位秒），请填写数字，例如：1、2、3")
    #
    #
    # case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
    #                                                                u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"磁力库"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return str(self.original_title)

    # def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}/testdatas/loginandcheckcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
    #     # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)
    #
    # go_to.short_description = u"复制新加"   #为go_to函数名个名字