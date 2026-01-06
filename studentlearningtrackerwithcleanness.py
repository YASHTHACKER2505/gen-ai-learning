def get_details():
    name = input("Enter your name: ")

    while True:
        try:
            course_count = int(input("How many topics are you learning? "))
            if course_count <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    topics = []
    for i in range(course_count):
        topic = input(f"Enter topic {i+1}: ")
        topics.append(topic)

    return name, topics


def update_progress(topics):
    progress = {}

    for topic in topics:
        while True:
            status = input(f"Is '{topic}' completed? (yes/no): ").lower()
            if status in ["yes", "no"]:
                progress[topic] = True if status == "yes" else False
                break
            else:
                print("Please enter only 'yes' or 'no'.")

    try:
        with open("progress.txt", "w") as f:
            for key, value in progress.items():
                f.write(f"{key}:{value}\n")
        print("Progress saved successfully.")
    except IOError:
        print("Error while saving progress to file.")

    return progress


def track_progress(progress):
    if not progress:
        print("No progress recorded yet.")
        return

    print("\nYour Progress:")
    for topic, status in progress.items():
        if status:
            print(f"{topic}  Completed")
        else:
            print(f"{topic}  Not completed")


def show_details(name, topics):
    print("\nStudent Details")
    print("----------------")
    print("Name:", name)
    print("Topics:", ", ".join(topics))


# MAIN PROGRAM
name, topics = get_details()
progress = {}

while True:
    print("\nMenu")
    print("1. Update progress")
    print("2. Track progress")
    print("3. Check details")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        progress = update_progress(topics)
    elif choice == 2:
        track_progress(progress)
    elif choice == 3:
        show_details(name, topics)
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
