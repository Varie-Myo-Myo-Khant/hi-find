from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from user.models import User
from chat.models import Message
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.db import connection
import json
import logging
logger = logging.getLogger('hi_find')

@api_view(['GET'])
def getAllMessageByReceiverId(request):
    user_id = request.GET.get("user_id")
    chat_mate = request.GET.get("chat_mate")
    query = f'select * from chat_message where (sender_id={user_id} and receiver_id={chat_mate}) or (sender_id={chat_mate} and receiver_id={user_id}) order by id asc'
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    messages = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    return JsonResponse(messages, safe=False)

@api_view(['POST'])
def sendMessage(request):
    data = json.loads(request.body.decode('utf-8'))
    Message.objects.create(receiver_id=data['receiver_id'], sender_id=data['sender_id'], message=data['message'])
    # return HttpResponse(new_message)
    return HttpResponse(status=200)

@api_view(['GET'])
def getChatList(request):
    user_id = request.GET.get('user_id')
    query = f'select u.id as mate_id, u.username, m.id, m.message, m.created_at, m.updated_at from signup_lostuser u, chat_message m where ((m.sender_id!={user_id} and m.sender_id=u.id) or (m.receiver_id!={user_id} and m.receiver_id=u.id)) and (m.sender_id={user_id} or m.receiver_id={user_id}) order by m.id desc'
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    chat_list = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    last_chat_user = []
    filtered_list = []
    for msg in chat_list:
        if(msg['mate_id'] in last_chat_user):
            continue
        else:
            filtered_list.append(msg)
            last_chat_user.append(msg['mate_id'])
    return JsonResponse(filtered_list, safe=False)

@api_view(['GET'])
def showChat(request):
    users = User.objects.all().values()
    return render(request, 'chat-trigger.html', { "users": users })