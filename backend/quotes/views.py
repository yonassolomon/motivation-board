from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Quote
from .serializers import QuoteSerializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def quote_list(request):
    if request.method=='GET':
        quotes=Quote.objects.filter(user=request.user)
        serializer=QuoteSerializer(quotes,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def quote_detail(request,pk):
    quote=get_object_or_404(Quote,pk=pk,user=request.user)
    if request.method=='PUT':
        serializer=QuoteSerializer(quote,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)