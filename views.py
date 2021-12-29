import os
import psycopg2
import pandas as pd
import json
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import TemplateSerializer, TemplateDeleteSerializer


class TemplateAPIView(APIView):
    permission_classes = (AllowAny,)

    serializer_class = TemplateDeleteSerializer
    def get(self, request, format=None):
        query_params = self.request.query_params
        createdby = query_params.get('createdby')
        templateName = query_params.get('templateName')
        try:
            con = psycopg2.connect(user=db_user, host=db_host, database=db_database, password=db_password)
            sql_data = pd.read_sql_query(f" select * from templateinfo where createdby = '{createdby}' and template_name = '{templateName}'; ", con)
            json_data = sql_data.to_json(orient="records")
            template_data = json.loads(json_data)
            return Response({'template_details': template_data})
        except:
            raise

    def post(self, request, format=None):
        serializer = TemplateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        createdby = serializer.validated_data['createdby']
        templateName = serializer.validated_data['templateName']
        templateData = serializer.validated_data['templateData']
        templatedatum = str(templateData)[1:-1]
        template_datum = templatedatum.replace("'", '"')
        print(createdby, templateName, template_datum)
        try:
            con = psycopg2.connect(user=db_user, host=db_host, database=db_database, password=db_password)
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            cur.execute(f"INSERT INTO public.templateinfo (createdby, template_name, template_data) VALUES('{createdby}', '{templateName}', '{template_datum}');")
            return Response(
                {
                    "success": True,
                    "message" : "Template Created Successfully..!"
                },
                status=status.HTTP_200_OK
            )
        except:
            raise

    def delete(self, request, format=None):
        serializer = TemplateDeleteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        createdby = serializer.validated_data['createdby']
        templateName = serializer.validated_data['templateName']
        print(createdby, templateName)
        try:
            con = psycopg2.connect(user=db_user, host=db_host, database=db_database, password=db_password)
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            cur.execute(f"DELETE FROM public.templateinfo WHERE createdby='{createdby}' AND template_name='{templateName}';")
            return Response(
                {
                    "success": True,
                    "message" : "Template Deleted Successfully..!"
                },
                status=status.HTTP_200_OK
            )
        except:
            raise
        
    def put(self, request, format=None):
        serializer = TemplateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "errors": serializer.errors
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        createdby = serializer.validated_data['createdby']
        templateName = serializer.validated_data['templateName']
        templateData = serializer.validated_data['templateData']
        templatedatum = str(templateData)[1:-1]
        template_datum = templatedatum.replace("'", '"')
        print(createdby, templateName, template_datum)
        try:
            con = psycopg2.connect(user=db_user, host=db_host, database=db_database, password=db_password)
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            cur.execute(f"UPDATE public.templateinfo SET template_data='{template_datum}' WHERE createdby='{createdby}' AND template_name='{templateName}';")
            return Response(
                {
                    "success": True,
                    "message" : "Template Details Updated Successfully..!"
                },
                status=status.HTTP_200_OK
            )
        except:
            raise
