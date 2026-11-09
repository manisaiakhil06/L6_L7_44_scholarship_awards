"""Defensive input parsing for scholarship applicant records."""
import math

def parse_applicant(text):
    """Parse ``category:marks``; malformed input returns an empty record."""
    if not isinstance(text, str) or text.count(":") != 1:
        return ("", 0.0)
    category, marks_text = text.split(":", 1)
    category = category.strip().title()
    try:
        marks = float(marks_text.strip())
    except (TypeError, ValueError, OverflowError):
        return ("", 0.0)
    if not category or not math.isfinite(marks) or marks < 0 or marks > 100:
        return ("", 0.0)
    return category, marks

def marks_average(marks_csv):
    """Return the integer average; invalid or empty CSV input returns zero."""
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        return 0
    parts = marks_csv.split(",")
    try:
        values = [int(part.strip()) for part in parts]
    except (TypeError, ValueError, OverflowError):
        return 0
    if not values or any(value < 0 or value > 100 for value in values):
        return 0
    return sum(values) // len(values)

def payable_award(text):
    """Compute award plus 18% less deduction; malformed values return 0.0."""
    if not isinstance(text, str) or text.count("|") != 1:
        return 0.0
    award_text, deduction_text = text.split("|", 1)
    try:
        award = float(award_text.strip())
        deduction = float(deduction_text.strip())
    except (TypeError, ValueError, OverflowError):
        return 0.0
    if not math.isfinite(award) or not math.isfinite(deduction) or award < 0 or deduction < 0:
        return 0.0
    return max(award * 1.18 - deduction, 0.0)

def main():
    print("==== Running parse_applicant ====")
    print("Category and Marks:", parse_applicant(input("Enter category:marks (e.g. merit:82): ")))
    print("\n==== Running marks_average ====")
    print("Average Marks:", marks_average(input("Enter marks as CSV (e.g. 72,85,90): ")))
    print("\n==== Running payable_award ====")
    print("Payable Award:", payable_award(input("Enter award|deduction (e.g. 5000|500): ")))

if __name__ == "__main__":
    main()
