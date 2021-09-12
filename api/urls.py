from django.urls import path
from api.views   import *

urlpatterns = [
                path('courses/new', course_new),
                path('courses/<int:course_id>delete', course_delete)
              ]
