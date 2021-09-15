from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validate(self, POST):
        errors = {}
        if len(POST['course_name']) < 5:
            errors['course_name'] = 'Name should be 5 or more characters long'
        return errors
    

    def serialize(self, course):
        return {
                 'id':          course.id,
                 'name':        course.name,
                 'description': course.description.text,
                 'created_at':  course.created_at.__format__('%b %d, %Y\n%I:%m %p'),
                 'updated_at':  course.updated_at.__format__('%b %d, %Y\n%I:%m %p')
               }

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
    
    
    def serialize(self, comment):
        return {
                 'id':         comment.id,
                 'course_id':  Course.objects.serialize(comment.course_id),
                 'first_name': comment.first_name,
                 'last_name':  comment.last_name,
                 'text':       comment.text,
                 'created_at':  course.created_at.__format__('%b %d, %Y %h:%s %p'),
                 'updated_at':  course.updated_at.__format__('%b %d, %Y %h:%s %p')
               }


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
