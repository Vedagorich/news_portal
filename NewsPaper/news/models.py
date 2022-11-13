from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def update_rating(self):
        pass


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    post = 'PO'
    news = 'NE'
    POSITIONS = [
        (post, 'Статья'),
        (news, 'Новость'),
    ]

    post_name = models.CharField(max_length=255)
    post_text = models.TextField(default="...")
    rating_post = models.IntegerField(default=0)
    post_news = models.CharField(max_length=2, choices=POSITIONS)
    time_post_add = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name

    def get_like_post(self):
        return self.rating_post

    def set_like_post(self, rating_post):
        rating_post =+ 1
        return rating_post


    def Dislike_post(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return f"{self.post_text[0:124]}..."


class Post_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_name = models.CharField(max_length=255)
    comment_text = models.TextField(default="...")
    comment_author = models.CharField(max_length=255)
    comment_time_add = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like_comment(self):
        self.rating_comment += 1
        self.save()

    def Dislike_comment(self):
        self.rating_comment -= 1
        self.save()
