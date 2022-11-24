
from django.contrib import admin
from django.urls import path
from KO.views import employeelistview, userlistview, employeedetailview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee', employeelistview),
    path('api/employee/<int:pk>', employeedetailview),
    path('api/user', userlistview),
]
