from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "reviews", verbose_name = "Користувач")
    content = models.TextField()
    publication_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.author.username
    
    class Meta:
        ordering = ["-publication_date"]
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"