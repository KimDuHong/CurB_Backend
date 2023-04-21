from rest_framework.serializers import ModelSerializer
from .models import Chattingroom, Message
from users.serializers import TinyUserSerializer
from users.models import User
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ParseError
from django.db.models import Q


class ChatroomSerialzier(ModelSerializer):
    user = TinyUserSerializer(read_only=True, many=True)
    # messages = serializers.MessageSerialzier(read_only=True, many=True)

    class Meta:
        model = Chattingroom
        fields = (
            "user",
            "created_at",
            # "messages",
        )


class MessageSerialzier(ModelSerializer):
    sender = TinyUserSerializer(read_only=True)
    room = ChatroomSerialzier(read_only=True)

    class Meta:
        model = Message
        fields = (
            "sender",
            "room",
            "text",
        )

    def create(self, validated_data):
        # 유저가 유효한지 확인
        validated_data["receiver"] = get_object_or_404(
            User, pk=validated_data.get("receiver")
        )
        print(validated_data)

        chatroom = (
            Chattingroom.objects.filter(user__in=[validated_data.get("sender")])
            .filter(user__in=[validated_data.get("receiver")])
            .first()
        )

        if not chatroom:
            chatroom = Chattingroom.objects.create()
            chatroom.user.add(validated_data.get("sender"))
            chatroom.user.add(validated_data.get("receiver"))

        return Message.objects.create(
            room=chatroom, sender=validated_data.get("sender")
        )