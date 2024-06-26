from django.db import models
from django.contrib.auth.models import User

# one to one
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='mypage')
    page_name = models.CharField(max_length=70)
    page_category = models.CharField(max_length=70)
    page_publish_date = models.DateField()

# many to one
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypost')
    post_title = models.CharField(max_length=70)
    post_category = models.CharField(max_length=70)
    post_publish_date = models.DateField()

# many to many
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def written_by(self):
        return ','.join([str(u) for u in self.user.all()])