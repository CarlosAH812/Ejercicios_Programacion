note_counter = 1
approved_notes_count = 0
failed_notes_count = 0
approved_notes_sum = 0
failed_notes_sum = 0
total_notes_average = 0

total_notes = int(input("Enter the total number of notes: "))

while note_counter <= total_notes:
    print(f"Enter the grade number {note_counter}")
    current_note = float(input("Grade: "))

    if current_note < 70:
        failed_notes_count += 1
        failed_notes_sum += current_note
    else:
        approved_notes_count += 1
        approved_notes_sum += current_note

    total_notes_average += (current_note / total_notes)

    note_counter += 1

if failed_notes_count > 0:
    failed_notes_average = failed_notes_sum / failed_notes_count
else:
    failed_notes_average = 0

if approved_notes_count > 0:
    approved_notes_average = approved_notes_sum / approved_notes_count
else:
    approved_notes_average = 0


print(f"The student has {approved_notes_count} approved grades.")
print(f"Average of approved grades: {approved_notes_average:.2f}")
print(f"The student has {failed_notes_count} failed grades.")
print(f"Average of failed grades: {failed_notes_average:.2f}")
print(f"Total average of all grades: {total_notes_average:.2f}")

