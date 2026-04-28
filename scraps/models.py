from django.db import models

class Scrap(models.Model):
    # The title of the bug or solution
    title = models.CharField(max_length=200)
    
    # Category tag (e.g., #DuskLight, #Arduino, #Django)
    project_tag = models.CharField(max_length=50)
    
    # The actual code snippet
    code_content = models.TextField()
    
    # Your notes on why this works or what it solves
    explanation = models.TextField()
    
    # Automatically saves the date and time when created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This makes it look nice in the admin panel
        return f"{self.project_tag} | {self.title}"