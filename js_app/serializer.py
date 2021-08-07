from rest_framework import serializers
from js_app.models import IDCode

class CodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(required=False, allow_null=True)
    img_url = serializers.CharField(required=False, allow_blank=True)
    code = serializers.CharField(required=False, allow_blank=True)
    content = serializers.CharField(required=False, allow_blank=True)
    # content = serializers.ListField(child=serializers.CharField(required=True, allow_blank=False))
    recognition = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = IDCode
        fields = ['id', 'created', 'img_url', 'code', 'content', 'recognition']

    def create(self, validated_data):
        """
        Create and return a new `IDCode` instance, given the validated data.
        """
        return IDCode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `IDCode` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.created = validated_data.get('created', instance.created)
        instance.img_url = validated_data.get('img_url', instance.img_url)
        instance.code = validated_data.get('code', instance.code)
        instance.content = validated_data.get('content', instance.content)
        instance.recognition = validated_data.get('recognition', instance.recognition)
        instance.save()
        return instance