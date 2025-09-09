from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


User = settings.AUTH_USER_MODEL

def upload_location(object, filename):
	return '{}/{}_{}'.format(object.author, object.slug, filename)


class Post(models.Model):
	subject = models.CharField(max_length=50)
	description = models.TextField()
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	image = models.ImageField(
		null=True,
		blank=True,
		upload_to=upload_location,
		height_field='height_field',
		width_field='width_field'
		)
	height_field = models.IntegerField(null=True, default=0)
	width_field = models.IntegerField(null=True, default=0)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=50, unique=True)
	publish_date = models.DateTimeField(null=True, blank=False, default=timezone.now())
	last_modify = models.DateTimeField(null=True, blank=True)
	hide = models.BooleanField(default=False)

	def __str__(self):
		return self.subject

	def get_absolute_url(self):
		return reverse("blog:post_detail", kwargs={"slug": self.slug})


class Category(models.Model):
	category = models.CharField(max_length=50)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = "Categories"


class Author(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	email = models.EmailField()
	#phone = PhoneField(blank=True, help_text='Contact Phone Number')

	def __str__(self):
		return self.user.username