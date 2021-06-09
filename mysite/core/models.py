from django.db import models

# Create your models here.


class News(models.Model):

    title = models.CharField(
        max_length=256,
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False
    )

    thumb_image = models.ImageField(
        upload_to='images/news/thumb/'
    )

    image = models.ImageField(
        upload_to='images/news/'
    )

    created_at = models.DateTimeField(
        auto_created=True
    )

    def __str__(self):
        return self.title


class Pet(models.Model):

    name = models.CharField(
        max_length=256,
        null=False,
        blank=False
    )

    pet_type = models.ForeignKey(
        'PetType',
        on_delete=models.CASCADE,
        null=True
    )

    description = models.TextField(
        null=False
    )

    image = models.ImageField(
        upload_to='images/news/'
    )

    created_at = models.DateTimeField(
        auto_created=True
    )

    def __str__(self):
        return self.name


class PetType(models.Model):

    title = models.CharField(
        max_length=256,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_created=True
    )

    def __str__(self):
        return self.title
