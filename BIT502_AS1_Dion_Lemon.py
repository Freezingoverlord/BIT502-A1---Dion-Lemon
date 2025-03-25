import os

#Dion Lemon
#BIT502
#5134899

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    #Main menu options
    clear_console()
    print("Welcome to The Aurora Archive")
    print("1. Membership Plans")
    print("2. Optional Extras")
    print("3. Reading Challenge")
    print("4. Aurora-Picks Rental Calculator")
    print("5. Exit the program")
    return input("Enter your selection: ")

def display_membership_plans():
    clear_console()
    print("Membership Plans")
    print("1. Standard")
    print("2. Premium")
    print("3. Kids")
    print("4. Return to main menu")
    print("5. Exit")
    return input("Enter your selection: ")

def display_membership_cost(plan):
    #Membership plan costs
    costs = {
        '1': ('Standard', 10),
        '2': ('Premium', 15),
        '3': ('Kids', 5)
    }
    if plan in costs:
        plan_name, monthly_cost = costs[plan]
        annual_cost = monthly_cost * 11
        print(f"{plan_name} Plan: ${monthly_cost}/month")
        print(f"Annual cost (1 month free): ${annual_cost}")
        print("Press any key to continue...")
        input()
    else:
        print("Invalid selection. Please try again.")
        input()

def display_optional_extras():
    clear_console()
    print("Optional Extras")
    print("1. Book rental: $5")
    print("2. Private area access: $15")
    print("3. Monthly booklet: $2")
    print("4. Online ebook rental: $5")
    print("5. Return to main menu")
    print("6. Exit")
    return input("Enter your selection: ")

def calculate_optional_extras():
    extras = {
        '1': ('Book rental', 5),
        '2': ('Private area access', 15),
        '3': ('Monthly booklet', 2),
        '4': ('Online ebook rental', 5)
    }
    total_cost = 0
    selected_extras = []
    for key, (name, cost) in extras.items():
        choice = input(f"Would you like {name} for ${cost} (yes/no)? ").strip().lower()
        if choice in ['yes', 'y']:
            total_cost += cost
            selected_extras.append(name)
    print("\nSelected Extras:")
    for extra in selected_extras:
        print(f"- {extra}")
    print(f"Total cost for extras: ${total_cost}")
    print("Press any key to return to the main menu...")
    input()

def kids_reading_challenge():
    clear_console()
    print("Welcome to the Reading Challenge. Please enter your pages read for each day.")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    pages_read = []
    for day in days:
        while True:
            try:
                pages = float(input(f"{day}: "))
                pages_read.append(pages)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    total_pages = sum(pages_read)
    average_pages = total_pages / len(days)
    max_pages = max(pages_read)
    max_days = [day for day, pages in zip(days, pages_read) if pages == max_pages]
    rank = get_reading_rank(total_pages)
    next_rank_pages = get_next_rank_pages(total_pages)
    print(f"\nTotal pages read: {total_pages}")
    print(f"Average pages per day: {average_pages:.1f}")
    print(f"Day(s) with most pages read: {', '.join(max_days)}")
    print(f"You ranked {rank}!")
    if next_rank_pages > 0:
        print(f"To reach the next rank you need to read {next_rank_pages} more pages. Good luck!")
    else:
        print("Congratulations! You have reached the highest rank!")
    print("Press any key to return to the main menu...")
    input()

def get_reading_rank(total_pages):
    if total_pages <= 25:
        return "Bronze"
    elif total_pages <= 50:
        return "Silver"
    elif total_pages <= 100:
        return "Gold"
    else:
        return "Platinum"

def get_next_rank_pages(total_pages):
    if total_pages <= 25:
        return 26 - total_pages
    elif total_pages <= 50:
        return 51 - total_pages
    elif total_pages <= 100:
        return 101 - total_pages
    else:
        return 0

def aurora_picks_rental_calculator():
    clear_console()
    print("Aurora-Picks Rental Calculator")
    print("1. Enter rental period")
    print("2. Return to main menu")
    return input("Enter your selection: ")

def calculate_rental_cost(days):
    if days < 3:
        return "Minimum rental period is 3 days."
    elif days > 21:
        return "Maximum rental period is 21 days."
    elif days == 21:
        return 12
    else:
        cost = 0
        if days <= 3:
            cost = 3
        elif days <= 8:
            cost = 3 + (days - 3) * 0.8
        else:
            cost = 3 + 5 * 0.8 + (days - 8) * 0.5
        return round(cost, 2)

def main():
    while True:
        choice = display_main_menu()
        if choice == '1':
            while True:
                plan_choice = display_membership_plans()
                if plan_choice == '4':
                    break
                elif plan_choice == '5':
                    exit()
                else:
                    display_membership_cost(plan_choice)
        elif choice == '2':
            calculate_optional_extras()
        elif choice == '3':
            kids_reading_challenge()
        elif choice == '4':
            while True:
                rental_choice = aurora_picks_rental_calculator()
                if rental_choice == '2':
                    break
                elif rental_choice == '1':
                    while True:
                        try:
                            days = int(input("Enter the number of days you wish to rent a book for: "))
                            cost = calculate_rental_cost(days)
                            if isinstance(cost, str):
                                print(cost)
                            else:
                                print(f"Total rental cost for {days} days: ${cost}")
                            break
                        except ValueError:
                            print("Invalid input. Please enter an integer.")
                    print("Press any key to return to the rental menu...")
                    input()
        elif choice == '5':
            print("Thank you for using The Aurora Archive system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
            input()

if __name__ == "__main__":
    main()
