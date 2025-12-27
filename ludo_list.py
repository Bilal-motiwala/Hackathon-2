players = []

while True:
    print("\n🎲 LUDO LIST APP 🎲")
    print("1. Add Player")
    print("2. View Players")
    print("3. Remove Player")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter player name: ")
        players.append(name)
        print("✅ Player added successfully!")

    elif choice == "2":
        if not players:
            print("⚠️ No players in the list.")
        else:
            print("\nPlayers List:")
            for i, player in enumerate(players, start=1):
                print(f"{i}. {player}")

    elif choice == "3":
        if not players:
            print("⚠️ No players to remove.")
        else:
            for i, player in enumerate(players, start=1):
                print(f"{i}. {player}")
            num = int(input("Enter player number to remove: "))
            if 1 <= num <= len(players):
                removed = players.pop(num - 1)
                print(f"❌ {removed} removed successfully!")
            else:
                print("❌ Invalid number!")

    elif choice == "4":
        print("👋 Exiting Ludo List. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
