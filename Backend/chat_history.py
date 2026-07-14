import os
import json
import uuid

def create_new_session():
    return str(uuid.uuid4())

class ChatHistory:

#-------------------------------CREATION OF STUDENT_ID FOLDER--------------------------------------------
    def __init__(self, student_id):

        base_directory = os.path.dirname(os.path.abspath(__file__))

        self.chat_folder = os.path.join(
            base_directory,
            "Chat_history",
            student_id
        )

        os.makedirs(self.chat_folder, exist_ok=True)


#-------------------------------SAVE MESSAGE--------------------------------------------
# It will save the chat history of a particular session by appending the new message
# to the existing messages in the JSON file.
    def save_message(self, session_id, role, content):

        filepath = os.path.join(
            self.chat_folder,
            f"{session_id}.json"
        )

        if os.path.exists(filepath):

            with open(filepath, "r") as file:
                data = json.load(file)

        else:

            data = {
                "session_id": session_id,
                "messages": []
            }

        data["messages"].append({
            "role": role,
            "content": content
        })

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

#-------------------------------LOAD MESSAGE--------------------------------------------
#It will load the chat history of a particular session.
    def load_chat(self, session_id):

        filepath = os.path.join(
            self.chat_folder,
            f"{session_id}.json"
        )

        if not os.path.exists(filepath):
            return None

        with open(filepath, "r") as file:
            return json.load(file)
        
#-------------------------------LIST SESSIONS--------------------------------------------
#This function will list all the sessions of a particular student by returning the names of 
# all the JSON files in the student's folder.
    def list_sessions(self):

            sessions = []

            for file in os.listdir(self.chat_folder):

                if file.endswith(".json"):

                    sessions.append(file.replace(".json", ""))

            return sessions