from django.shortcuts import render, redirect
from mainsite         import data

# Create your views here.
def index(request):
    context = data.index()
    return render(request, 'mainsite/index.html', context)

def course(request, course_id):
    context = data.context()
    return render(request, 'mainsite/comments.html', context)


def course_new(request):
    data.course_new(request)
    return redirect('/')


def course_confirm_delete(request, course_id):
    context = data.course_confirm_delete(request, course_id)
    return render(request, 'mainsite/confirm_delete.html', context)


def course_delete(request, course_id):
    result = data.course_delete(request, course_id)
    return redirect('/')


def comment_new(request, course_id):
    course = Course.objects.get(id=course_id)
    errors = Comment.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f'/course/{course_id.id}')
    Comment.objects.create(
                            course_id  = course,
                            first_name = request.POST['commenter_first_name'],
                            last_name  = request.POST['commenter_last_name'],
                            text       = request.POST['comment']
                          )
    messages.success(request, f'Your comment was successfully logged.')
    return redirect(f'/courses/{course_id}')
