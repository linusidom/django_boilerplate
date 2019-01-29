from rest_framework import generics
from '+app_name+'.api.models import '+app_name.title()+'Serializer
from '+app_name+'.models import '+app_name.title()+'

class '+app_name.title()+RUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = '+app_name.title()+'Serializer
	queryset = '+app_name.title()+'.objects.all()'