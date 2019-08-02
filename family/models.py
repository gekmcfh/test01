from django.db import models


class Parent(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title


class Child(models.Model):
    title = models.CharField(
        max_length=150,
    )
    parents = models.ManyToManyField(
        Parent,
        blank=True
    )

    def __str__(self):
        return self.title
