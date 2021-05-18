"""
NHTSA has a public api; the url we will be working with is 
https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=1

This api endpoint returns JSON; it has the field 'Results' - a list of car manufacturers with details.
We want to create a dictionary with country as a key, and list of manufacturer names as a value, e.g:
{
    'USA': ['Tesla', 'Ford', ...],
    'Japan': ['Honda', 'Subaru', ...]
}
Use 'Mfr_Name' as a manufacturer name.
If 'Country' is empty - skip it. We should traverse through all pages of this api endpoint

bad.py has a finished implementation of this task. Your goal is to make this code better, in any
way you can think of. Put your solution in good.py
Some examples of what can be done:
- you can create your own iterator/generator to go through pages for you
- insertion of items into dictionary can be improved

Also, add more tests to the test_dict.py to check response content.
"""
from collections import defaultdict
from typing import Dict, List

import requests


def response_pages(url):
    page = 1
    while True:
        response = requests.get(f"{url}&page={page}").json()
        if not response["Count"]:
            break
        else:
            page += 1
            yield response


def create_country_make_dict(url: str) -> Dict[str, List[str]]:
    country_manufacturers = defaultdict(list)

    for page_response in response_pages(url):
        for result in page_response["Results"]:
            country = result["Country"]
            if country:
                country_manufacturers[country].append(result["Mfr_Name"])
    return country_manufacturers
