import re
from datetime import datetime

def extract_experiences(text):
    """
    Extract role, company, and dates
    """
    pattern = r"(.*?) at (.*?) from ([A-Za-z]+ \d{4}) to ([A-Za-z]+ \d{4}|Present)"
    matches = re.findall(pattern, text)

    experiences = []
    for role, company, start, end in matches:
        experiences.append({
            "role": role.strip(),
            "company": company.strip(),
            "start": start.strip(),
            "end": end.strip()
        })

    return experiences


def is_current_job(end_date):
    if end_date.lower() == "present":
        return True

    try:
        end = datetime.strptime(end_date, "%B %Y")
        return end > datetime.now()
    except:
        return False


def calculate_total_experience(experiences):
    total_months = 0

    for exp in experiences:
        try:
            start = datetime.strptime(exp["start"], "%B %Y")

            if exp["end"].lower() == "present":
                end = datetime.now()
            else:
                end = datetime.strptime(exp["end"], "%B %Y")

            total_months += (end.year - start.year) * 12 + (end.month - start.month)

        except:
            continue

    years = total_months // 12
    months = total_months % 12

    return f"{years} years {months} months"