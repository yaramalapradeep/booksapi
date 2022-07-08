from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book,Employee
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def booklist(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def book_detail(request, id):
    if request.method == 'GET':
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        book = Book.objects.get(pk=id)
        book.delete()
        return Response("object  deleted successfully")

#Django View function to send HttpResponse with json data
import json
from django.http import HttpResponse,JsonResponse
def emp_data_json_view(request):
    emp_data={'eno':1, 'ename':'pradeep', 'esal':3000 }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data)

def emp_data_json_response(request):
    emp_data = {'eno': 1, 'ename': 'pradeep', 'esal': 30000}
    return JsonResponse(emp_data)

from django.views.generic import View
class JsonCbv(View):
    def get(self, *args, **kwargs):
        emp_data = {'eno': 1, 'ename': 'pradeep kumar', 'esal': 30000}
        return JsonResponse(emp_data)

#Mixin example

from .mixins import JsonResponseMixin,HttpResponseMixin
class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        emp_data = {'eno': 1, 'ename': 'yaramala pradeep kumar', 'esal': 30000}
        return self.render_to_json_response(emp_data)

#performing database crud operations by using webapi without REST framework
from django.core.serializers import serialize

class EmployeeCRUDcbv(View):

    def get(self,request,id, *args, **kwargs):
        employee = Employee.objects.get(id=id)
        json_data = serialize('json', [employee], fields=('eno','ename'))
        return HttpResponse(json_data, content_type='application/json')

#To get all employees

# class EmployeeListCBV(View):
#     def get(self,request, *args, **kwargs):
#         employees = Employee.objects.all()
#         emp_data = serialize('json', employees)
#         pdict = json.loads(emp_data)
#         final_list =[]
#         for obj in pdict:
#             final_list.append(obj['fields'])
#         return HttpResponse(final_list)

from .mixins import SerializeMixin
class EmployeeListCBV2(SerializeMixin, View):
    def get(self,request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')


from .utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'please send valid json data only'}), status=400)
        json_data = json.dumps({'msg':'post method'})
        return self.render_to_http_response(json_data)







