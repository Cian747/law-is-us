from django.db import models

class Attorney(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='attorneys/')
    linkedin = models.URLField(blank=True)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Attorneys'

    def __str__(self):
        return self.name

class PracticeArea(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    image = models.ImageField(upload_to='practice_areas/')

    def __str__(self):
        return self.title

class FAQ(models.Model):
    category = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.question

class Testimonial(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author} - {self.role}"

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at}"