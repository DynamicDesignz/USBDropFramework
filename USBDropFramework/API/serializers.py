from API.models import TargetData
from rest_framework import serializers

class TargetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TargetData
        fields = ('ip_address', 'computer_name', 'target_id', 'test_id')
