from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

class tfRequestResponseViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = timefhumanRequestResponse.objects.all()
    serializer_class = tfRequestResponseSerializer

    def create(self, request):
        serializer = tfRequestResponseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            ds = serializer.data['detected_date_response']

            if ds!="":
                message = "Booking a meeting appointment on " + ds[24:26] + "/" + ds[17:19] + "/" + ds[6:10] + " at " + ds[32:34] + ":" + ds[43:45] + " " + request.data['timezone']
            else:
                message = "timefhuman failed to detect date!!"

            data_sent = {
              "entries":[
                {
                  "template_type":"message",
                  "message":message,
                  "full_width" : False,
                  "text_color" : '#484848',
                  "background_color":  '#f5f5f5',
                  "script": 'console.log("hello")',
                }
              ]
            }

            return Response(data_sent)

        return Response({"status":"Bad Request"})

class spRequestResponseViewSet(viewsets.ModelViewSet):
    queryset = spacyRequestResponse.objects.all()
    serializer_class = spRequestResponseSerializer

    def create(self, request):
        serializer = spRequestResponseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            ds = serializer.data['entity_detect_response']

            av=[]

            for key,value in eval(ds).items():
                av.append({"attribute":"request_" + value.lower(),"value":key})

            data_sent = {
              "entries":[
                {
                  "template_type":"set_attr",
                  "attributes":av
                }
              ]
            }

            return Response(data_sent)

        return Response({"status":"Bad Request"})

"""class dkRequestResponseViewSet(viewsets.ModelViewSet):
    queryset = ducklingRequestResponse.objects.all()
    serializer_class = dkRequestResponseSerializer

    def create(self, request):
        serializer = dkRequestResponseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            ds = serializer.data['duckling_response']

            message = ds

            data_sent = {
              "entries":[
                {
                  "template_type":"message",
                  "message":message,
                  "full_width" : False,
                  "text_color" : '#484848',
                  "background_color":  '#f5f5f5',
                  "script": 'console.log("hello")',
                }
              ]
            }

            return Response(data_sent)

        return Response({"status":"Bad Request"})"""
