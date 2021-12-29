from rest_framework import serializers

class TemplateSerializer(serializers.Serializer):
    createdby = serializers.CharField()
    templateName = serializers.CharField(max_length=230)
    templateData = serializers.JSONField()

class TemplateDeleteSerializer(serializers.Serializer):
    createdby = serializers.CharField()
    templateName = serializers.CharField(max_length=230)
