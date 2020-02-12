from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

# Post.objects.all()
# Post.objects.create()
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return (
            super(PostManager, self)
            .filter(draft=False)
            .filter(publish__lte=timezone.now())
        )


def upload_location(instance, filename):
    # return f"{instance.pk}/{filename}"
    # print(instance.user.id)
    return "{}/{}".format(instance.pk, filename)


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
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
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/posts/{self.id}"
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id", "-timestamp", "-updated"]


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = f"{slug}-{qs.first().id}"
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_receiver(sender, instance, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)


# pre_save.connect(pre_save_receiver, sender=Post)


# @receiver(pre_save, sender=Post)
# def my_handler(sender, **kwargs):
#     pass
