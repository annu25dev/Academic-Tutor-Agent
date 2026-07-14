import json
import os
import uuid
from datetime import datetime

def create_new_student():

    student_id = str(uuid.uuid4())

    filename = f"{student_id}.json"

    StudentMemory(filename)

    return student_id

#----------------------------------STUDENT PROFILE--------------------------------------------
class StudentMemory:

    def __init__(self, filename):
        #Creating a emory file to store a student's personal details
        base_directory=os.path.dirname(os.path.abspath(__file__))
        #This creates diffrent student profiles
        self.student_memory_file_path=os.path.join(base_directory, filename)
        self.initialize_memory()

    # Create JSON if it doesn't exist
    def initialize_memory(self):

        base_directory = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(base_directory, exist_ok=True)

        if not os.path.exists(self.student_memory_file_path):
            #DEFAULT_PARAMETERS
            default_memory = {
                 "student_id": os.path.splitext(
                     os.path.basename(self.student_memory_file_path)
                    )[0],

                "student_profile": {
                    "name": "",
                    "school":"",
                    "stream":"",
                    "college":"",
                    "college_degree":"",
                    "specification":"",
                    "learning_level":"",
                    "class":"",
                    "year":"",
                },
                "student_learning_history": [],
                "saved_quizzes": [],
                "saved_plans": []
            }

            #write JSON
            with open(self.student_memory_file_path, "w") as file:
                json.dump(default_memory, file, indent=4)

    # Read JSON
    def load_memory(self):

        with open(self.student_memory_file_path, "r") as file:
            return json.load(file)

    # Save JSON
    def save_memory(self, memory):

        with open(self.student_memory_file_path, "w") as file:
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

    def update_learning_history(self, topic):

            memory = self.load_memory()

            history = memory.get("student_learning_history", [])

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Step 1: Complete any topic currently in progress
            for item in history:
                if item["status"] == "In Progress":
                    item["status"] = "Completed"
                    item["timestamp"] = timestamp

            # Step 2: Check if this topic already exists
            for item in history:

                if item["topic"].lower() == topic.lower():

                    item["status"] = "In Progress"
                    item["timestamp"] = timestamp

                    self.save_memory(memory)

                    return {
                        "status": "success",
                        "message": f"{topic} updated successfully."
                    }

            # Step 3: Add new topic
            history.append({
                "topic": topic,
                "status": "In Progress",
                "timestamp": timestamp
            })

            self.save_memory(memory)

            return {
                "status": "success",
                "message": f"{topic} added successfully."
            }

    def get_learning_history(self):

        memory = self.load_memory()

        return memory.get("student_learning_history", [])
    
#----------------------------------QUIZ SAVING AND RETRIEVAL------------------------------------

    def save_quiz(self, topic, quiz):

        memory = self.load_memory()

        quiz_object = {
            "topic": topic,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "quiz": quiz
        }

        memory["saved_quizzes"].append(quiz_object)

        self.save_memory(memory)

        return {
            "status": "success",
            "message": f"Quiz results for {topic} saved successfully."
        }

    def get_saved_quizzes(self):
        memory = self.load_memory()

        return memory.get("saved_quizzes", [])
    
#----------------------------------PLANNER SAVING AND RETRIEVAL------------------------------------

    def save_plan(self, topic, plan):

        memory = self.load_memory()

        planner_object = {
            "topic": topic,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "plan": plan
        }

        memory["saved_plans"].append(planner_object)

        self.save_memory(memory)

        return {
            "status": "success",
            "message": f"Study Plan for {topic} saved successfully."
        }

    def get_saved_plans(self):
        memory = self.load_memory()

        return memory.get("saved_plans", [])
