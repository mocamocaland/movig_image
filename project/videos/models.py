from django.db import models


class Video(models.Model):
    """moving image"""

    title = models.CharField('動画タイトル', max_length=255)
    description = models.TextField('説明(空欄可)', blank=True)
    thumbnail = models.ImageField('サムネイル', upload_to='thumbnails/', null=True, blank=True) # /media/thumbnails/filename
    upload = models.FileField('ファイル', upload_to='uploads/%y/%m/%d/') # /media/uploads/2018/3/20 path
    
    created_at = models.DateTimeField('作成日', auto_now_add=True) # 入力欄は表示されない
    updated_at = models.DateTimeField('更新日', auto_now=True) # 更新するたびに日時が格納される

    def __str__(self):
        return self.title
