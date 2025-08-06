from django.db import models

class Review(models.Model):
    username = models.CharField(max_length = 200)
    text = models.TextField()
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-date"]
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"