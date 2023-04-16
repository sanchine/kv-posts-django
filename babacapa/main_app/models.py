from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    username = models.CharField(max_length=40)
    text = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('Картинка', upload_to='posts/', blank=True, null=True)
    audio = models.FileField('Трек', upload_to='tracks/', blank=True, null=True)
    like_count = models.IntegerField('Лайк', default=0)

    def __str__(self):
        max_strLen = 75
        if len(self.text) > max_strLen:
            return self.text[:max_strLen] + '...'
        else:
            return self.text

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

