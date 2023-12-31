from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import *

def homeApp(request):
    return render(request, "home.html")

def download(request, uid):
    return render(request, "download.html", context= {"uid": uid})

class HandleFileUpload(APIView):

    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializers(data = data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status" : 200,
                    "message" : "files uploaded successfully",
                    "data" : serializer.data
                })
            
            return Response({
                "status" : 400,
                "message" : "something went wrong",
                "data" : serializer.errors
            })
        
        except Exception as e:
            print(e)
