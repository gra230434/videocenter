from django.db import models


def AnimatePath(instance):
    return instance.Animate.animateEN


# Create your models here.
class Animate(models.Model):
    animate = models.CharField(max_length=256)
    animateEN = models.CharField(max_length=256)
    Image = models.ImageField(upload_to=AnimatePath)
    update = models.DateField.auto_now()

    def __str__(self):
        return self.animate


class AnimateDetail(models.Model):
    Season_Chice = (
        ('1', 'Winter'),
        ('2', 'Spring'),
        ('3', 'Summer'),
        ('4', 'Autumn'),
        )
    animate = models.CharField(max_length=256)
    animateEN = models.CharField(max_length=256)
    sequence = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    season = models.CharField(max_length=1, choices=Season_Chice)
    is_end = models.BooleanField(default=True)
    Image = models.ImageField(upload_to=AnimatePath)
    ImageBig = models.ImageField(upload_to=AnimatePath)
