from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    author=models.models.CharField(max_length=150,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}:{self.text[:30]}"
