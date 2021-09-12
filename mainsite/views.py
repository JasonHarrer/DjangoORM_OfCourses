from django.contrib   import messages
from django.shortcuts import render, redirect
from mainsite.models  import Course, Description

# Create your views here.
def index(request):
    context = { 
                'courses': Course.objects.all()
             }
    return render(request, 'mainsite/index.html', context)


def course(request):
    pass


def course_new(request):
    errors = Course.objects.validate(request.POST)
    errors.update(Description.objects.validate(request.POST))
    if len(errors ) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')

    new_course = Course.objects.create(name=request.POST['course_name'])
    new_description = Description.objects.create(course_id = new_course,
                                                 text      = request.POST['course_description'])
    messages.success(request, f'Course {new_course.name} successfully created')
    return redirect('/')



def course_delete(request, course_id):
    context = {
                'course': Course.objects.get(id=course_id)
              }
    return render(request, 'mainsite/delete.html', context)


def course_confirm_delete(request):
    pass
