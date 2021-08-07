from js_app.models import IDCode
from js_app.serializer import CodeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from src import captcha
import time
import json
import requests
from requests import Request, Session

from js_app.utils import IDCodeFormater

class IDCodeList(APIView):
    """
    List all IDCodeList, or create a new IDCode.
    """
    # def get(self, request, format=None):
    #     idcodes = IDCode.objects.all()
    #     serializer = CodeSerializer(idcodes, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        idcode = request.data
        serializer = CodeSerializer(data=idcode)
        if serializer.is_valid():
            session = Session()
            request = Request('GET', idcode['img_url'], headers={'User-Agent': 'Mozilla/5.0'})
            prepped = session.prepare_request(request)
            resp = session.send(prepped)

            # recognition the code
            cap = captcha.TextSelectCaptcha()
            data_all = cap.run(resp.content)
            formater = IDCodeFormater()
            
            #data = formater.get_target(res=data_all, target_str=idcode['content'])
            data = formater.format(res=data_all, target_str=idcode['content'])

            serializer.validated_data['recognition'] = data_all
            serializer.save()

            return Response(data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IDcodeDetail(APIView):
    """
    Retrieve, update or delete a idcode instance.
    """
    def get_object(self, pk):
        try:
            return IDCode.objects.get(pk=pk)
        except IDCode.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idcode = IDCode.objects.get(pk=pk)
        serializer = CodeSerializer(idcode)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        idcode = self.get_object(pk)
        serializer = CodeSerializer(idcode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idcode = self.get_object(pk)
        IDCode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)