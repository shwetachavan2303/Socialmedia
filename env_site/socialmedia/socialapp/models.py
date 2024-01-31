from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
User= get_user_model()

class profile(models.Model):
    user= models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE)
    Discription=models.TextField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True ,upload_to="profile_images")
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class meta:
        db_table ="profile"
        
class Post(models.Model):
    user = models.ForeignKey(User,related_name="post",on_delete=models.CASCADE)
    captions=models.TextField()
    image = models.ImageField(blank=True,null=True,upload_to="post_images")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class meta:
        db_table ="Post"
        
class likepost(models.Model):
    post=models.ForeignKey(Post,related_name="like_post",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="like_post",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class meta:
        db_table ="like_post"