# Patient Data Processing Pipeline
# Healthcare Analytics - with Column Masking

import datetime

# Masking helper functions
def mask_name(name):
    parts = name.split()
    masked = []
    for part in parts:
        if len(part) <= 1:
            masked.append(part)
        else:
            masked.append(part[0] + "*" * (len(part) - 2) + part[-1])
    return " ".join(masked)

def mask_phone(phone):
    return "*" * (len(phone) - 4) + phone[-4:]

# Sample patient data with phone numbers added
patients = [
    {"id": 1, "name": "Raj Kumar",    "age": 45, "phone": "9876543210", "diagnosis": "Diabetes",     "admitted": True},
    {"id": 2, "name": "Priya Singh",  "age": 32, "phone": "9123456780", "diagnosis": "Hypertension", "admitted": False},
    {"id": 3, "name": "Anil Mehta",   "age": 60, "phone": "9988776655", "diagnosis": "Diabetes",     "admitted": True},
    {"id": 4, "name": "Sunita Rao",   "age": 28, "phone": "9001122334", "diagnosis": "Asthma",       "admitted": False},
    {"id": 5, "name": "Vikram Das",   "age": 55, "phone": "9765432100", "diagnosis": "Hypertension", "admitted": True},
    {"id": 6, "name": "Meera Patel",  "age": 38, "phone": "9345678901", "diagnosis": "Diabetes",     "admitted": True},
]

# Apply masking
def apply_masking(patients, mask=True):
    result = []
    for p in patients:
        row = p.copy()
        if mask:
            row["name"]  = mask_name(p["name"])
            row["phone"] = mask_phone(p["phone"])
        result.append(row)
    return result

# Simulate two views
print("=" * 55)
print("  VIEW 1 — MASKED (for analysts/junior staff)")
print("=" * 55)
masked_patients = apply_masking(patients, mask=True)
print(f"{'ID':<4} {'Name':<15} {'Phone':<14} {'Age':<5} {'Diagnosis'}")
print("-" * 55)
for p in masked_patients:
    print(f"{p['id']:<4} {p['name']:<15} {p['phone']:<14} {p['age']:<5} {p['diagnosis']}")

print()
print("=" * 55)
print("  VIEW 2 — UNMASKED (for authorized doctors only)")
print("=" * 55)
unmasked_patients = apply_masking(patients, mask=False)
print(f"{'ID':<4} {'Name':<15} {'Phone':<14} {'Age':<5} {'Diagnosis'}")
print("-" * 55)
for p in unmasked_patients:
    print(f"{p['id']:<4} {p['name']:<15} {p['phone']:<14} {p['age']:<5} {p['diagnosis']}")

print()
# Summary
total = len(patients)
avg_age = sum(p["age"] for p in patients) / total
admitted = sum(1 for p in patients if p["admitted"])
print("=" * 55)
print(f"  Total Patients    : {total}")
print(f"  Average Age       : {avg_age:.1f} years")
print(f"  Currently Admitted: {admitted}")
print("=" * 55)
