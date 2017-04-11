# _*_ coding:utf-8 _*_
from django.db import models

# Create your models here.


# Create your models here.
class Question(models.Model):
    question_text = models.CharField('题目编写',max_length=200)
    pub_date = models.DateTimeField('时间选择')
#    sort = models.SmallIntegerField('排序')                    # 排序
    
    def __unicode__(self):
        return self.question_text
    
    class Meta:
        verbose_name = '题目'
        verbose_name_plural = '题目'
#        ordering = ['sort']     # 排序

class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name='选项所属题目' )
    choice_text = models.CharField(max_length=200, verbose_name='选项' )
    votes = models.IntegerField(default=0, verbose_name='票数' )
    
    def __unicode__(self):
        return self.choice_text
        
    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项'
    