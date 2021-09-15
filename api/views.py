from django.http      import JsonResponse
from django.shortcuts import render
from mainsite         import data

# Create your views here.
def course_new(request):
    return JsonResponse(data.course_new(request))


def course_delete(request, course_id):
    return JsonResponse(data.course_delete(request, course_id))
