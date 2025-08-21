# Student Management System (revamped)
# - One-line inputs
# - Search by Roll or Name
# - Aligned table view
# - Safe delete with confirmation

students = []

# ---------- Utilities ----------
def pause():
    input("\nPress Enter to continue...")

def find_index_by_roll(roll_no):
    for i, s in enumerate(students):
        if s["roll_no"] == roll_no:
            return i
    return -1

def print_table(rows):
    """rows is a list of dicts with keys: roll_no, name, grade, age"""
    if not rows:
        print("No records found.")
        return
    roll_w  = max(4, max(len(str(r["roll_no"])) for r in rows))
    name_w  = max(4, max(len(str(r["name"]))    for r in rows))
    grade_w = max(5, max(len(str(r["grade"]))   for r in rows))
    age_w   = max(3, max(len(str(r["age"]))     for r in rows))

    header = f"{'Roll':<{roll_w}}  {'Name':<{name_w}}  {'Grade':<{grade_w}}  {'Age':>{age_w}}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{str(r['roll_no']):<{roll_w}}  "
            f"{str(r['name']):<{name_w}}  "
            f"{str(r['grade']).upper():<{grade_w}}  "
            f"{str(r['age']):>{age_w}}"
        )

# ---------- Add Student ----------
def add_student():
    print("\n=== Add Student ===")
    details = input("Enter details (Roll, Name, Grade, Age): ").strip()
    parts = [p.strip() for p in details.split(",")]

    if len(parts) < 3:
        print("❌ Invalid input. Provide at least: Roll, Name, Grade")
        pause()
        return

    roll_no = parts[0]
    name    = parts[1]
    grade   = parts[2]
    age     = parts[3] if len(parts) > 3 and parts[3] else "N/A"

    # Unique roll check
    if find_index_by_roll(roll_no) != -1:
        print("⚠️ Roll number already exists! Try a different roll.")
        pause()
        return

    students.append({"roll_no": roll_no, "name": name, "grade": grade, "age": age})
    print("✅ Student added successfully!")
    pause()

# ---------- View Students ----------
def view_students():
    print("\n=== Student Records ===")
    print_table(students)
    pause()

# ---------- Search Student ----------
def search_student():
    print("\n=== Search Student ===")
    mode = input("Search by (1) Roll  or  (2) Name: ").strip()

    if mode == "1":
        roll = input("Enter roll: ").strip()
        idx = find_index_by_roll(roll)
        if idx == -1:
            print("❌ Student not found.")
        else:
            print_table([students[idx]])
    elif mode == "2":
        key = input("Enter name (full or part): ").strip().lower()
        matches = [s for s in students if key in s["name"].lower()]
        if matches:
            print_table(matches)
        else:
            print("❌ No students matched that name.")
    else:
        print("❌ Invalid choice.")
    pause()

# ---------- Update Student ----------
def update_student():
    print("\n=== Update Student ===")
    target_roll = input("Enter roll number of the student to update: ").strip()
    idx = find_index_by_roll(target_roll)
    if idx == -1:
        print("❌ Student not found.")
        pause()
        return

    s = students[idx]
    print("Current:")
    print_table([s])

    print("\nEnter new details as one line. Leave blanks to keep existing.")
    print("Format: Roll, Name, Grade, Age")
    print("Example to change only name & age:  , Sneha, , 22")
    raw = input("New details: ").strip()
    parts = [p.strip() for p in raw.split(",")] if raw else []
    while len(parts) < 4:
        parts.append("")

    new_roll  = parts[0] or s["roll_no"]
    new_name  = parts[1] or s["name"]
    new_grade = parts[2] or s["grade"]
    new_age   = parts[3] or s["age"]

    # If roll changed, ensure uniqueness
    if new_roll != s["roll_no"] and find_index_by_roll(new_roll) != -1:
        print("⚠️ Another student already has that roll. Update cancelled.")
        pause()
        return

    students[idx] = {"roll_no": new_roll, "name": new_name, "grade": new_grade, "age": new_age}
    print("✅ Student updated successfully!")
    pause()

# ---------- Delete Student ----------
def delete_student():
    print("\n=== Delete Student ===")
    roll_no = input("Enter roll number to delete: ").strip()
    idx = find_index_by_roll(roll_no)
    if idx == -1:
        print("❌ Student not found.")
        pause()
        return

    s = students[idx]
    print("About to delete:")
    print_table([s])
    confirm = input(f"Are you sure you want to delete {s['name']} (y/n)? ").strip().lower()
    if confirm == "y":
        del students[idx]
        print("🗑️ Student deleted successfully!")
    else:
        print("❌ Deletion cancelled.")
    pause()

# ---------- Exit ----------
def exit_program():
    print("\n👋 Exiting Student Management System... Goodbye!")
    raise SystemExit

# ---------- Main Menu ----------
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if     choice == "1": add_student()
        elif   choice == "2": view_students()
        elif   choice == "3": search_student()
        elif   choice == "4": update_student()
        elif   choice == "5": delete_student()
        elif   choice == "6": exit_program()
        else: print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
