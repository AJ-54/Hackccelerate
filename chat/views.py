from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from .models import Chat
from accounts.models import User
# from django.shortcuts import get_object_or_404



def get_curent_chat(chatId):
    return get_object_or_404(Chat,id=chatId)


def get_last_10_messages(chatId):
    
    chat = get_object_or_404(Chat,id=chatId)
    return chat.messages.order_by('-timestamp')[:10]

def chat(request, chat_id):
    return render(request, 'chat/chat.html', {
        'room_name':mark_safe(json.dumps(chat_id)),
        'username' : mark_safe(json.dumps(request.user.username or ""))

    })
