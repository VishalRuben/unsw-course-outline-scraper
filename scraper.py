import requests
import json
import html
import sys


def get_offering_url(course_code, term, year):
    """
    Step 1: Search for the course and find the correct offering.
    We extract the secondaryURL, which contains all offering parameters.
    """

    base_url = "https://courseoutlines.unsw.edu.au/v1/publicsitecourseoutlines/search"

    params = {
        "searchText": course_code,
        "year": year,
        "pageNumber": 1,
        "top": 10,
        "orderBy": "coursename desc",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    results = data.get("response", {}).get("results", [])

    # Find the exact offering matching course code + term + year
    for item in results:
        if (
            item.get("integrat_coursecode") == course_code
            and item.get("integrat_term") == term
            and item.get("integrat_year") == str(year)
        ):
            return item.get("secondaryURL")

    print(
        f"Error: No offering found for {course_code} in {term} {year}. "
        "It may not be offered in that term."
    )
    sys.exit(1)


def scrape_course_outline_from_url(url):
    """
    Step 2: Fetch the outline using the full offering URL.
    """

    response = requests.get(url)
    data = response.json()

    if data.get("integrat_coursecode") is None:
        print("Error: Outline not found even though offering exists.")
        sys.exit(1)

    # Extract assessments
    assessments_json = data.get("integrat_CO_Assessment", [])
    assessments = []
    for assessment in assessments_json:
        assessments.append(
            {
                "assessment_name": assessment.get("integrat_title", ""),
                "assessment_type": assessment.get("integrat_groupindividual", ""),
                "weighting": assessment.get("integrat_weight", ""),
                "due_date": assessment.get("integrat_duedate", ""),
                "description": html.unescape(assessment.get("integrat_summary", "")),
                "hurdles": assessment.get("integrat_hurdlerules", ""),
                "learning_outcomes": assessment.get("integrat_assmtclos", []),
            }
        )

    # Build final result
    result = {
        "course_code": data.get("integrat_coursecode"),
        "course_title": data.get("integrat_coursename"),
        "course_term": data.get("integrat_term"),
        "course_year": data.get("integrat_year"),
        "course_aims": html.unescape(data.get("integrat_courseaims", "")),
        "attendance_requirements": data.get("integrat_attendancereq"),
        "campus": data.get("integrat_campus"),
        "career": data.get("integrat_career"),
        "assessments": assessments,
    }

    return result


if __name__ == "__main__":
    course_code = (
        sys.argv[1]
        if len(sys.argv) > 1
        else input("Enter course code (e.g. COMP1511): ")
    )
    term = sys.argv[2] if len(sys.argv) > 2 else input("Enter term (e.g. Term 1): ")
    year = sys.argv[3] if len(sys.argv) > 3 else input("Enter year (e.g. 2024): ")

    # Step 1: Find offering URL
    offering_url = get_offering_url(course_code, term, year)

    # Step 2: Scrape outline using offering URL
    output = scrape_course_outline_from_url(offering_url)

    # Save JSON
    filename = f"{course_code}_{term}_{year}.json"
    with open(filename, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Saved to {filename}")
