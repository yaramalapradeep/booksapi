
from django.urls import path
from .views import booklist,book_detail,emp_data_json_view,emp_data_json_response,JsonCbv,JsonCBV2, EmployeeCRUDcbv, EmployeeListCBV
urlpatterns = [
    path('books/', booklist, name='booklist'),
    path('book/<int:id>', book_detail, name='book_detail'),
    path('empdata/', emp_data_json_view, name='emp_data_json_view'),
    path('emp-json-response/', emp_data_json_response, name='emp_data_json_view'),
    path('emp-JsonCbv-response/', JsonCbv.as_view(), name='emp_data_json_view'),
    path('emp-JsonCbv2-response/', JsonCBV2.as_view(), name='emp_data_json_view'),
    path('EmployeeCRUDcbv/<int:id>', EmployeeCRUDcbv.as_view(), name='EmployeeCRUDcbv' ),
    path('EmployeeListCBV2/', EmployeeListCBV.as_view(), name='EmployeeListCBV2'),

   ]