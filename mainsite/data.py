from django.contrib   import messages

from mainsite.models  import *


def index():
    return { 
             'courses': Course.objects.all()
           }


def course():
    return {
             'course': Course.objects.get(id=course_id),
             'comments': Comment.objects.filter(course_id=course_id).order_by('-created_at')
           }


def course_new(request):
    errors = Course.objects.validate(request.POST)
    errors.update(Description.objects.validate(request.POST))
    if len(errors ) > 0:
        for error in errors.values():
            messages.error(request, error)
        return { 'success': False }
            
    new_course = Course.objects.create(name=request.POST['course_name'])
    new_description = Description.objects.create(course_id = new_course,
                                                 text      = request.POST['course_description'])
    messages.success(request, f'Course {new_course.name} successfully created')
            
    return {
             'success': True,
             'course': Course.objects.serialize(new_course)
           }


def course_get(request, course_id):
        return {
                 'success': True,
                 'course': Course.objects.serialize(Course.objects.get(id=course_id))
               }


def course_confirm_delete(request, course_id):
    return {
             'course': Course.objects.get(id=course_id)
           }
    
    
def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return {
             'success': True
           }
