from django.db import models
from tinymce import models as tmcemodel

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    # This method is called when somebody tried to print this model object
    def __str__(self) -> str:
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    # This method is called when somebody tried to print this model object

    def __str__(self) -> str:
        return self.name


class BlogTags(models.Model):
    name = models.CharField(max_length=100)
    # This method is called when somebody tried to print this model object

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    #
    image = models.ImageField()
    title = models.CharField(max_length=255)
    # relation to author
    # Many Blogs written by one another
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    # relation with category
    # many blogs inside one category
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT)
    # many blogs linked in many tags
    tags = models.ManyToManyField(BlogTags, blank=True)
    short_description = models.TextField(default="")
    description = tmcemodel.HTMLField()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title


class BlogComment(models.Model):
    comment = models.TextField()
    full_name = models.CharField(max_length=100)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # many comments in one blogs
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)
