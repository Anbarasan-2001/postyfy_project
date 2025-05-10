from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', default='default.jpg')
    caption = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)  # <-- Add this line

    def __str__(self):
        return f"Post by {self.user.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    @property
    def profile_image_url(self):
        return self.profile_image.url


class Image(models.Model):
    title = models.CharField(max_length=255)  # Title for the image
    image = models.ImageField(upload_to='images/')  # The image itself
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the image is created

    def __str__(self):
        return self.title

def some_view(request):
    from core.models import Image
    # Example view logic for querying Image objects
    images = Image.objects.all()  # Query all Image objects
    return render(request, 'some_template.html', {'images': images})
