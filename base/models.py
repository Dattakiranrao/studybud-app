from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Room(models.Model):
    # User is use to connect the many to one relation
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Topic is use to connect the many to one relation
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # name = models.CharField(max_length=200)  # null is default flase such that it is required if set true it means it can be skipped
    description = models.TextField(
        null=True, blank=True
    )  # blank is for the form such that the description can be empty in a form element
    participants = models.ManyToManyField(
        User, related_name="participants", blank="true"
    )
    updated = models.DateTimeField(auto_now=True)  # time stap when updated
    created = models.DateTimeField(
        auto_now_add=True
    )  # auto now add takes the time only when created un like on saving for auto_now

    class Meta:
        ordering = ["-updated", "-created"]

    def ___str__(self):
        return self.name

    objects = models.Manager()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # room = models.ForeignKey(Room, on_delete=models.SET_NULL) # database relation ships set null means when the attached room gets deleted set the foreignkey to null
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # database relation ships cascade means delete the message if the room gets deleted better for space managment
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # time stap when updated
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[0:50]

    objects = models.Manager()
