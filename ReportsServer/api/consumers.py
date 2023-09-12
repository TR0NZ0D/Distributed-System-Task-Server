from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from . import models


# class WebsocketNotificationsConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_group_name = "ptws_client_notifications_group"

#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)  # type: ignore

#         await self.accept()  # type: ignore

#     async def disconnect(self, code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)  # type: ignore

#     async def notification(self, event):
#         notification_object = await self.get_notification_object(event['notification_id'])
#         notification_object.read = True
#         await sync_to_async(notification_object.save)()
#         await self.send(text_data=event["html"])  # type: ignore

#     @database_sync_to_async
#     def get_notification_object(self, id: int):
#         return models.NotificationModel.objects.get(id=id)
