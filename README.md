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
  - assessments
- supports command line usage
- automaticaly saves results to <COURSE_CODE_TERM_YEAR>.json
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

Run the scraper by typing:

python scraper.py

into the terminal. There is also support for typing the course, term and year as command line arguments. For example:

python scraper.py COMP1511 Term 1 2024

However if no command line arguments are provided, the script will prompt inputs.

This will:

- print the course data to the terminal
- save it to COMP1511_Term 1_2024.json in the project folder

If no course/term/year is provided, it will print an error.

HOW IT WORKS
The script sends GET requests to the official UNSW Course Outlines API:
https://courseoutlines.unsw.edu.au/v1/publicsitecourseoutlines/search
https://courseoutlines.unsw.edu.au/v1/publicsitecourseoutlines/detail

It passes the provided parameters:

- course code
- year
- term

The API returns structured JSON, which the script extracts and formats.

EXAMPLE OUTPUT

Check in the COMP1511_Term 1_2024.json file.

REQUIREMENTS

- Python 3.9+
- requests

LICENSE

MIT License
