UNSW COURSE OUTLINE SCRAPER

A lightweight Python tool that fetches official UNSW course outline data directly from the public UNSW Course Outlines API.

FEATURES

- Fetches course information using the UNSW public API
- Outputs clean JSON with:
  - course code
  - course title
  - course aims
  - attendance requirements
  - campus
  - career
- supports command line usage
- automaticaly saves results to <COURSE_CODE>.json
- Minimal dependencies (requests only)

INSTALLATION

Clone the repository:
git clone https://github.com/VishalRuben/unsw-course-outline-scraper.git
cd unsw-course-outline-scraper

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

USAGE

Run the scraper with a course code:
python scraper.py COMP1511

If no course code is provided, it defaults to COMP1511.

This will:

- print the course data to the terminal
- save it to COMP1511.json in the project folder

HOW IT WORKS
The script sends a GET request to the official UNSW Course Outlines API:
https://courseoutlines.unsw.edu.au/v1/publicsitecourseoutlines/detail

It passes parameters such as:

- course code
- year
- term
- delivery mode
- campus

The API returns structured JSON, which the script extracts and formats.

EXAMPLE OUTPUT
{
"course_code": "COMP1511",
"course_title": "Programming Fundamentals",
"course_aims": "The importance of this course lies in its role...",
"attendance_requirements": "Students are strongly encouraged to attend all classes...",
"campus": "Sydney",
"career": "Undergraduate"
}

REQUIREMENTS

- Python 3.9+
- requests

LICENSE

MIT License

FUTURE IMPROVEMENTS

Add error handling for invalid course codes
Add support for checking multiple terms
Add parsing for assessment requirements
