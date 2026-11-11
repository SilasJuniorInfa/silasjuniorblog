from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_adress = models.EmailField(max_length=254)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

        
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.caption}"


class Posts(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name="posts")
    excerpt = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return f"{self.title}, {self.author}"
    

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    
    class Meta:
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return f"{self.user_name} commented on {self.post}"
    
    
        
    