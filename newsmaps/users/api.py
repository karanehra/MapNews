# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status ,viewsets, response
from rest_framework.decorators import list_route
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):

	@list_route(methods = ['POST'])
	def add_user(self, request):
		first_name = request.data["first_name"]
		last_name = request.data["last_name"]
		email = request.data["email"]
		username = request.data["username"]

		response = {}

		try:
			user = User.objects.get(username = username)
			response['status'] = 0
			response['data'] = 'Username Exists!'
		except:
			user = User(first_name = first_name, last_name= last_name, email = email, username = username)
			user.save()
			response['status'] = 1
			response['data'] = 'User Created'

		return Response(response , status=status.HTTP_200_OK)



	@list_route(methods = ['POST','GET'])
	def user_list(self,request):
		response = {}
		users = User.objects.all()
		serializer  = UserSerializer(users, many=True)
		response['data'] = serializer.data
		print response
		return Response(response, status=status.HTTP_200_OK)

