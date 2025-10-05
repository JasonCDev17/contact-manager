import sqlite3

# Connect to database
conn = sqlite3.connect("contacts.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    city TEXT
)
""")

# Add sample data if empty
if not cur.execute("SELECT 1 FROM contacts").fetchone():
    sample_data = [
        ("James West", "james.west@example.com", "+44 7700 900123", "London"),
        ("Mark East", "mark.east@example.com", "+44 7700 900234", "Manchester"),
        ("Annie South", "annie.south@example.com", "+44 7700 900345", "Birmingham"),
        ("Kerry North", "kerry.north@example.com", "+44 7700 900456", "Liverpool")
    ]
    cur.executemany("INSERT INTO contacts (name, email, phone, city) VALUES (?, ?, ?, ?)", sample_data)
    conn.commit()

# Menu loop
while True:
    print("\n📇 CONTACT MANAGER")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("→ Choose an option: ")

    if choice == "1":
        for row in cur.execute("SELECT * FROM contacts"):
            print(row)

    elif choice == "2":
        data = (
            input("Name: "),
            input("Email: "),
            input("Phone: "),
            input("City: ")
        )
        cur.execute("INSERT INTO contacts (name, email, phone, city) VALUES (?, ?, ?, ?)", data)
        conn.commit()
        print("✅ Contact added!")

    elif choice == "3":
        cid = input("Enter ID to update: ")
        new_city = input("Enter new city: ")
        cur.execute("UPDATE contacts SET city=? WHERE id=?", (new_city, cid))
        conn.commit()
        print("✅ Contact updated!")

    elif choice == "4":
        cid = input("Enter ID to delete: ")
        cur.execute("DELETE FROM contacts WHERE id=?", (cid,))
        conn.commit()
        print("🗑️ Contact deleted!")

    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, please try again.")

conn.close()
