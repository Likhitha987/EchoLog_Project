from django.db import models
from django.contrib.auth.models import User

class Scrap(models.Model):
    # This links the scrap to a specific user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scraps')
    title = models.CharField(max_length=200)
    project_tag = models.CharField(max_length=50)
    explanation = models.TextField()
    code_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __cl__(self):
        return self.title