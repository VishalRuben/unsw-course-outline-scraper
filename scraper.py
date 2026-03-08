import requests
import json
import html
import sys


def scrape_course_outline(
    course_code="COMP1511",
    year=2026,
    term="Term 1",
    delivery_mode="In Person",
    delivery_format="Standard",
    teaching_period="T1",
    delivery_location="Kensington",
    activity_group_id=1,
):
    base_url = "https://courseoutlines.unsw.edu.au/v1/publicsitecourseoutlines/detail"

    params = {
        "year": year,
        "term": term,
        "deliveryMode": delivery_mode,
        "deliveryFormat": delivery_format,
        "teachingPeriod": teaching_period,
        "deliveryLocation": delivery_location,
        "courseCode": course_code,
        "activityGroupId": activity_group_id,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    result = {
        "course_code": data.get("integrat_coursecode"),
        "course_title": data.get("integrat_coursename"),
        "course_aims": html.unescape(data.get("integrat_courseaims", "")),
        "attendance_requirements": data.get("integrat_attendancereq"),
        "campus": data.get("integrat_campus"),
        "career": data.get("integrat_career"),
    }

    return result


if __name__ == "__main__":
    course_code = sys.argv[1] if len(sys.argv) > 1 else "COMP1511"
    output = scrape_course_outline(course_code)

    with open(f"{course_code}.json", "w") as f:
        json.dump(output, f, indent=4)

    print(json.dumps(output, indent=4))
