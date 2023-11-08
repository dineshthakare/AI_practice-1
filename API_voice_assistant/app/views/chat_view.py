# app/views/user_view.py
from flask import jsonify
from app.controllers.chat_controller import ChatController

chat_controller = ChatController()  # Pass mongo_db object during instantiation


class ChatView:
    def __init__(self, chat_controller):
        self.chat_controller = chat_controller

    def chat(self, request):
        chat = self.chat_controller.chat(request)
        return jsonify(chat), 201

    def get_chats(self):
        return jsonify(self.chat_controller.get_chats()), 200

    def chat_Voice(self, request):
        chat = self.chat_controller.chat_Voice(request)
        return jsonify(chat), 201

    def get_Chats_Voice(self):
        return jsonify(self.chat_controller.get_chats_Voice()), 200
