from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def hello_word(request):
#     return Response({'msg':'hello world'})

@api_view(['POST'])
def hello_word(request):
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'hello worlds h'})

