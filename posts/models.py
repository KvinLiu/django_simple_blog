from django.db import models
from django.urls import reverse


def upload_location(instance, filename):
    # return f"{instance.pk}/{filename}"
    print(instance.user.id)
    return "{}/{}".format(instance.pk, filename)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    # image = models.FileField(null=True, blank=True)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field",
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    context = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/posts/{self.id}"
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-id", "-timestamp", "-updated"]
