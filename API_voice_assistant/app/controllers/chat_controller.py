from flask import jsonify, request
from datetime import datetime, timedelta
from app import mongo_db
from dotenv import load_dotenv
from datetime import datetime
from app.service.chat_service import chat_service

load_dotenv()


class ChatController:
    def chat(self, request):
        data = request.get_json()
        command = data.get("command")
        response = chat_service(command)
        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%H:%M")
        if response:
            mongo_payload = {
                "command": command,
                "response": response,
                "time": currentTime,
            }
        else:
            mongo_payload = {
                "command": command,
                "response": "Sorry! Can you say again?",
                "time": currentTime,
            }
        chat_id = mongo_db.chats.insert_one(mongo_payload).inserted_id
        chats = mongo_db.chats.find({}, {})
        chat_list = []
        for x in chats:
            chat_list.append(
                {
                    "_id": str(x["_id"]),
                    "command": x["command"],
                    "response": x["response"],
                    "time": x["time"],
                }
            )
        response_data = {"data": chat_list}
        return response_data, 200

    def get_chats(self):
        chats = mongo_db.chats.find({}, {})
        chat_list = []
        for x in chats:
            chat_list.append(
                {
                    "_id": str(x["_id"]),
                    "command": x["command"],
                    "response": x["response"],
                    "time": x["time"],
                }
            )
        response_data = {"data": chat_list}
        return response_data, 200

    def chat_Voice(self, request):
        data = request.get_json()
        command = data.get("command")
        response = chat_service(command)
        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%H:%M")
        if response:
            mongo_payload = {
                "command": command,
                "response": response,
                "time": currentTime,
            }
        else:
            mongo_payload = {
                "command": command,
                "response": "Sorry! Can you say again?",
                "time": currentTime,
            }
        chat_id = mongo_db.chats.insert_one(mongo_payload).inserted_id
        chats = mongo_db.chats.find({}, {})
        chat_list = []
        for x in chats:
            chat_list.append(
                {
                    "_id": str(x["_id"]),
                    "command": x["command"],
                    "response": x["response"],
                    "time": x["time"],
                }
            )
        response_data = {"data": chat_list}
        return response_data, 200

    def get_chats_Voice(self):
        chats = mongo_db.chats.find({}, {})
        chat_list = []
        for x in chats:
            chat_list.append(
                {
                    "_id": str(x["_id"]),
                    "command": x["command"],
                    "response": x["response"],
                    "time": x["time"],
                }
            )
        response_data = {"data": chat_list}
        return response_data, 200
