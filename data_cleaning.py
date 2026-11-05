"""Clean sample student records by removing duplicates and invalid entries."""


def sample_records():
    return [
        {"id": 1, "name": "Asha", "age": 21, "city": "Delhi"},
        {"id": 2, "name": "Rahul", "age": 23, "city": "Jaipur"},
        {"id": 2, "name": "Rahul", "age": 23, "city": "Jaipur"},
        {"id": 3, "name": "", "age": 20, "city": "Agra"},
        {"id": 4, "name": "Neha", "age": 17, "city": "Delhi"},
        {"id": 5, "name": "Vikas", "age": 25, "city": "Lucknow"},
        {"id": 6, "name": "Meera", "age": None, "city": "Jaipur"},
    ]


def clean_records(records, minimum_age=18):
    """Return unique adult records with a non-empty name and valid age."""
    if not isinstance(minimum_age, int) or minimum_age < 0:
        raise ValueError("minimum_age must be a non-negative integer")

    cleaned = []
    seen_ids = set()
    for record in records:
        if not isinstance(record, dict):
            continue
        record_id = record.get("id")
        name = record.get("name")
        age = record.get("age")
        if record_id is None or record_id in seen_ids:
            continue
        if not isinstance(name, str) or not name.strip():
            continue
        if isinstance(age, bool) or not isinstance(age, int) or age < minimum_age:
            continue
        cleaned.append({**record, "name": name.strip()})
        seen_ids.add(record_id)
    return cleaned


if __name__ == "__main__":
    records = sample_records()
    cleaned = clean_records(records)
    print(f"Original records: {len(records)}")
    print("Cleaned records:")
    for record in cleaned:
        print(record)
    print(f"Cleaned record count: {len(cleaned)}")
