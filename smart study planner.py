import json
import os
from pdb import main
def load_session():
    if os.path.exists('study-log.txt'):
          with open('study-log.txt', 'r') as f:
               return json.load(f)
    return {}
def save_session(session):
    with open('study-log.txt', 'w') as f:
        json.dump(session, f, indent=4)
def classification_session(duration):
    if duration < 30:
        return 'Short'
    elif duration < 60:
         return'Medium'
    else:
         return 'Long'

def add_session(sessions):
    print("\n--- Add a New Study Session ---")

    topic = input("Enter the topic: ")
    date = input("Enter the date: ")

    while True:
        dur_input = input("Enter minutes: ")

        try:
            duration = float(dur_input)

            if duration <= 0:
                print("Please enter a positive number for duration.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    new_session = {
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(new_session)
    save_session(sessions)     

    print("Study session added successfully!")

def view_sessions(sessions):
    print("\n--- All Study Sessions ---")

    if not sessions:
        print("No study sessions found.")
        return

    for i, session in enumerate(sessions, start=1):
         print(f"{i}. Topic: {session['topic']}, Date: {session['date']}, Duration: {session['duration']} minutes")
def study_statistics(sessions):
            if not sessions:
                print("not data.")
                return

            total_mins = sum(session['duration'] for session in sessions)

            print(f"Total hours studied: {total_mins/60:.2f} hours")

            subject_totals = {}

            for session in sessions:
                subject = session['subject']
                duration = session['duration']
                if subject in subject_totals:
                    subject_totals[subject] += duration
                else:
                    subject_totals[subject] = duration

            print("/nHours per subject:")
            for subject,min in subject_totals.items():
                print(f"{subject}: {min/60:.2f} hours")

            weakest_subject=min(subject_totals, key=subject_totals.get)
            print(f"Weakest subject: {weakest_subject}({subject_totals[weakest_subject]/60:.2f} hours)")

            longest=max(sessions, key=lambda s: s['duration'])
            print(f"Longest study session:{longest['topic']} ({longest['duration']} minutes)")

            def main():
                sessions=load_session()
                print(f"Welcome!loaded {len(sessions)} study sessions.")

while True:
     print("\n---Smart Study Planner---")
     print("1. Add a new study session")
     print("2. View all study sessions")
     print("3. Search by subject")
     print("4. View study statistics")
     print("5. Save and Exit")

     choice=input("choose an option: ")
     if choice=='1':
         add_session(sessions)

     elif choice=='2':
         view_sessions(sessions)

     elif choice=='3':
         search_by_subject(sessions)

     elif choice=='4':
          study_statistics(sessions)

     elif choice=='5':
         save_session(sessions)
         print("Sessions saved. Goodbye!")
         break

     else:
         print("Invalid option. Pick 1 to 5.")

if __name__ == "__main__":
    main()
           
     
     


     




 
