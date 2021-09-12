from django.urls import path
from mainsite.views import *


urlpatterns = [
                path('', index),
                path('courses/new', course_new),

                path('courses/<int:course_id>', course),
                path('courses/<int:course_id>/new', comment_new),


                path('courses/<int:course_id>/delete', course_delete),
                path('courses/<int:course_id>/confirm_delete', course_confirm_delete)

              ]
