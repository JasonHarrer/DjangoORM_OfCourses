from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validate(self, POST):
        errors = {}
        if len(POST['course_name']) < 5:
            errors['course_name'] = 'Name should be 5 or more characters long'
        return errors


class Course(models.Model):
    name        = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = CourseManager()


class DescriptionManager(models.Manager):
    def validate(self, POST):
        errors = {}
        if len(POST['course_description']) < 15:
            errors['course_description'] = 'Description should be 15 or more characters long'
        return errors


class Description(models.Model):
    course_id   = models.OneToOneField(Course, on_delete=models.CASCADE)
    text        = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = DescriptionManager()


class CommentManager(models.Manager):
    def validate(self, POST):
        errors = {}
        return errors


class Comment(models.Model):
    course_id   = models.ForeignKey(Course, on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    text        = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = CommentManager()

    @property
    def commenter(self):
        return f'{self.first_name} {self.last_name}'
