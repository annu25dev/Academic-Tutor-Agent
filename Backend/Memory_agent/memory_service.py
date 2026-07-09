import json
import os
from datetime import datetime

#Creating a memory file
MEMORY_FILE = "Backend/Memory_agent/student_memory.json"

#----------------------------------STUDENT PROFILE--------------------------------------------
class StudentMemory:

    def _init_(self):
        self.initialize_memory()

    # Create JSON if it doesn't exist
    def initialize_memory(self):

        os.makedirs("Backend/Memory_agent", exist_ok=True)

        if not os.path.exists(MEMORY_FILE):

            memory = {
                "student_profile": {},
                "student_learning_history": []
            }

            #write JSON
            with open(MEMORY_FILE, "w") as file:
                json.dump(memory, file, indent=4)

    # Read JSON
    def load_memory(self):

        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    # Save JSON
    def save_memory(self, memory):

        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=4)

    # Update profile
    def update_profile(self, profile):

        memory = self.load_memory()

        memory["student_profile"].update(profile)

        self.save_memory(memory)

        return "Student profile updated successfully."

    # Retrieve profile
    def get_profile(self):

        memory = self.load_memory()

        return memory["student_profile"]

#----------------------------------PREVIOUS LEARNING HISTORY------------------------------------


    def update_learning_history(self, topic, status):

        memory = self.load_memory()

        history = memory.get("student_learning_history", [])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update existing topic
        for item in history:

            if item["topic"].lower() == topic.lower():

                item["status"] = status
                item["timestamp"] = timestamp

                self.save_memory(memory)

                return {
                    "status": "success",
                    "message": f"{topic} updated successfully."
                }

        # Add new topic
        history.append({
            "topic": topic,
            "status": status,
            "timestamp": timestamp
        })

        memory["student_learning_history"] = history

        self.save_memory(memory)

        return {
            "status": "success",
            "message": f"{topic} added successfully."
        }

    def get_learning_history(self):

        memory = self.load_memory()

        return memory.get("student_learning_history", [])