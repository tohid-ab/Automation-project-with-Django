from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NameeNegari(models.Model):
    CH = (
        ('low', 'کم'),
        ('normal', 'معمولی'),
        ('much', 'زیاد')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=CH)
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'نامه نگاری'
        verbose_name_plural = 'نامه ها'

    def __str__(self):
        return self.title