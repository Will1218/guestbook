from django.db import models

# Create your models here.
class Message(model.Model):
    user = model.CharField('姓名', max_length = 50)
    reciever = model.CharField('收件人', max_length = 50)
    subject = model.CharField('主旨', max_length = 60)
    cotent = models.TextField('內容')
    created = models.DateTimeField('留言時間', auto_now_add = True)

    def __str__(self):
        return self.user + ':' + self.subject