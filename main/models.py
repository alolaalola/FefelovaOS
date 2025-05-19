from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # ← ДОБАВЬ ЭТО

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.author

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
