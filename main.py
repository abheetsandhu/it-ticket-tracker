"""
IT Ticket Tracker

This program simulates a basic IT support ticket tracking system.
It allows users to add tickets, view tickets, update ticket status,
and summarize open/closed tickets.
"""

tickets = []


def add_ticket():
    name = input("Enter user's name: ")
    issue = input("Enter issue description: ")
    priority = input("Enter priority (Low/Medium/High): ")

    ticket = {
        "id": len(tickets) + 1,
        "name": name,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    tickets.append(ticket)
    print("Ticket added successfully.\n")


def view_tickets():
    if not tickets:
        print("No tickets found.\n")
        return

    print("\nAll Tickets")
    print("-----------")

    for ticket in tickets:
        print(f"Ticket ID: {ticket['id']}")
        print(f"User: {ticket['name']}")
        print(f"Issue: {ticket['issue']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print("--------------------")

    print()


def update_ticket_status():
    try:
        ticket_id = int(input("Enter ticket ID to update: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            new_status = input("Enter new status (Open/In Progress/Closed): ")
            ticket["status"] = new_status
            print("Ticket status updated successfully.\n")
            return

    print("Ticket not found.\n")


def ticket_summary():
    open_count = 0
    closed_count = 0
    in_progress_count = 0

    for ticket in tickets:
        if ticket["status"].lower() == "open":
            open_count += 1
        elif ticket["status"].lower() == "closed":
            closed_count += 1
        elif ticket["status"].lower() == "in progress":
            in_progress_count += 1

    print("\nTicket Summary")
    print("--------------")
    print(f"Open Tickets: {open_count}")
    print(f"In Progress Tickets: {in_progress_count}")
    print(f"Closed Tickets: {closed_count}\n")


def main():
    while True:
        print("IT Ticket Tracker")
        print("1. Add Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. View Ticket Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket_status()
        elif choice == "4":
            ticket_summary()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.\n")


main()
