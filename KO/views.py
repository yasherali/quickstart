from .models import Employee
from .serializers import EmployeeSerializers, UserSerializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def employeelistview(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        serializer = EmployeeSerializers(employee, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['DELETE', 'GET', 'PUT'])
def employeedetailview(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=404)

    if request.method == "DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "GET":
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EmployeeSerializers(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def userlistview(request):
    if request.method=='GET':
        users= User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)
