from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    text = models.TextField()
    date_created =models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

    def _str_(self):
        return self.title



