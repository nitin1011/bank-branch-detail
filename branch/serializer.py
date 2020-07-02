from rest_framework import serializers
from .models import Branch, Bank


class BranchDetailSerializer(serializers.ModelSerializer):


	class Meta:
		model = Branch
		fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']