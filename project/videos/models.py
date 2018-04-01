from django.db import models


class Video(models.Model):
    """moving image"""

    title = models.CharField('動画タイトル', max_length=255)
    descritption = models.TextField('説明(空欄可)', blank=True)
    thumbnail = models.ImageField('サムネイル', )
