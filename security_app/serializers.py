from rest_framework import serializers
from .models import Channel
from users.models import CustomUser




# class ChannelSerializer(serializers.ModelSerializer):
#     sender_user = serializers.CharField(source='sender_user.email', read_only=True)
#
#     class Meta:
#         model = Channel
#         fields = ['sender_user', 'recipient_user', 'name']


class ChannelSerializer(serializers.ModelSerializer):
    sender_user = serializers.CharField(source='sender_user.email', read_only=True)
    recipient_user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.none())

    class Meta:
        model = Channel
        fields = ['sender_user', 'recipient_user', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request', None)
        if request:
            self.fields['recipient_user'].queryset = CustomUser.objects.exclude(id=request.user.id)

    def create(self, validated_data):
        validated_data['sender_user'] = self.context['request'].user
        return super().create(validated_data)



    # def get_recipient_user(self, obj):
    #     request = self.context.get('request', None)
    #     if request is None:
    #         return []
    #
    #     current_user_email = request.user.email
    #     all_users = User.objects.exclude(email=current_user_email)
    #     return [user.email for user in all_users]


class ChannelSenderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'sender_user']


class ChannelRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'recipient_user']
