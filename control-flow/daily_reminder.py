# Step 1: Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2 & 3: Process the Task and Provide a Customized Reminder
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task with time sensitivity. Plan accordingly.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Complete it when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task but time-bound. Don’t delay too much.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority input. Please enter 'high', 'medium', or 'low'.")
