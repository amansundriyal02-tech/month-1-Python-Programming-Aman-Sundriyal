"""
Client Project: Basic data cleaning
- Remove duplicate records.
- Remove records with missing required values.
- Filter records using a simple condition.
"""


def sample_records():
    return [
        {"id": 1, "name": "Asha", "age": 21, "city": "Delhi"},
        {"id": 2, "name": "Rahul", "age": 23, "city": "Jaipur"},
        {"id": 2, "name": "Rahul", "age": 23, "city": "Jaipur"},  # duplicate
        {"id": 3, "name": "", "age": 20, "city": "Agra"},         # missing name
        {"id": 4, "name": "Neha", "age": 17, "city": "Delhi"},
        {"id": 5, "name": "Vikas", "age": 25, "city": "Lucknow"},
        {"id": 6, "name": "Meera", "age": None, "city": "Jaipur"}, # missing age
    ]


def clean_records(records, minimum_age=18):
    """
    Return unique records with a name and valid age, keeping adults only.
    Duplicate detection uses the record ID.
    """
    cleaned = []
    seen_ids = set()

    for record in records:
        record_id = record.get("id")
        name = record.get("name")
        age = record.get("age")

        if record_id in seen_ids:
            continue
        if not name or age is None:
            continue
        if not isinstance(age, int) or age < minimum_age:
            continue

        cleaned.append(record.copy())
        seen_ids.add(record_id)

    return cleaned


if __name__ == "__main__":
    original = sample_records()
    result = clean_records(original)
    print("Original records:", len(original))
    print("Cleaned records:")
    for item in result:
        print(item)
    print("Cleaned records:", len(result))
