from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Publisher(AbstractUser):
    years_of_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "publisher"
        verbose_name_plural = "publishers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("agency:publisher-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Publisher, related_name="newspapers")

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} ({self.published_date})"
