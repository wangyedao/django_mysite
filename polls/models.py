from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(
'问题内容',max_length=200)
    pub_data = models.DateField('发布时间')

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""
   类被翻译成SQL执行：
   CREATE table question(
        id int primary key increase
        question_text char(200) comment'问题内容'
        pub_data datetime comment"发布时间"

)
   CREATE table votes if not exists(
        id int primary key increase,
        choice_text char(200) comment"选项内容"，
        votes int default 0 comment"投票数"
        question int,
        foriegn key question reference question.id on 
   ) 
"""
# django自带orm框架，用法类似SQLalchemy
# 自定义的类要集成prm框架中的MODEL类，这样orm框架能把类和数据库联系起来