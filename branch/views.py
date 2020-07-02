from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import BranchDetailSerializer
from .models import Branch, Bank
from rest_framework.response import Response
# Create your views here.


def index(request):
	return render(request, 'branch.html', {})


@api_view(['GET'])
def branch_detail(request):

	'''
	Fetch the detail of branch using its ifsc code
	'''

	ifsc = request.GET.get('ifsc')					# take input from url
	branch = Branch.objects.get(ifsc=ifsc)			# fetch data from the branch table 
	serial = BranchDetailSerializer(branch)			# convert output into JSON formate
	return Response(data=serial.data)				# return response


@api_view(['GET'])
def branch_all(request):

	'''
	Fetch the detail of all branchs using bank name and city
	'''

	bank_name = request.GET.get('bank_name')						# take bank name input from url 
	city = request.GET.get('city')									# take city input from url
	bank = Bank.objects.get(name=bank_name)							# fetch bank detail from bank table
	branch = Branch.objects.filter(bank_id=bank.bank_id, city=city)	# fetch branch detail from branch table
	serial = BranchDetailSerializer(branch, many=True)				# convert output into JSON formate
	return Response(data=serial.data)								# return response