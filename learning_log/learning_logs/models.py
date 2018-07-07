from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    #属性text是一个CharField由字符或文本组成的数据，可以储存像名称、标题。定义charfield时要告诉Django该数据库中预留多少空间
    text = models.CharField(max_length = 2000) 
    #data_added是一个DataTimeField记录日期和时间的数据，每当用户创建新主题时，都让Django将这个属性自动设置成当前日期和时间
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User)
    
    
    #我们需要告诉Django,默认使用哪个属性来显示有关主题的信息。调用方法__str__来显示模型的简单表示，返回储存在属性text中的字符串
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
    
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """返回模型字符串表示"""
        return self.text[:50] + "..."