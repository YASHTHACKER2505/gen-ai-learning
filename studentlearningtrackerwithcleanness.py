def get_details():
    name = input("Enter your name: ")
    course_count = int(input("How many topics are you learning? "))

    topics = []
    for i in range(course_count):
        topic = input(f"Enter topic {i+1}: ")
        topics.append(topic)

    return name, topics


def update_progress(topics):
    progress = {}
    for topic in topics:
        status = input(f"Is '{topic}' completed? (yes/no): ").lower()
        progress[topic] = True if status == "yes" else False

    with open("progress.txt", "w") as f:
        for k, v in progress.items():
            f.write(f"{k}:{v}\n")

    print("Progress saved successfully.")
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
    print("\nName:", name)
    print("Topics:", topics)


# MAIN PROGRAM
name, topics = get_details()
progress = {}

while True:
    print("\n1. Update progress")
    print("2. Track progress")
    print("3. Check details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        progress = update_progress(topics)
    elif choice == "2":
        track_progress(progress)
    elif choice == "3":
        show_details(name, topics)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
