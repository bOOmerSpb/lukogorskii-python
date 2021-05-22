from itertools import chain

import pytest

from bad import create_country_make_dict as bad_dict
from good import create_country_make_dict as good_dict

REQUEST_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_dict_length(dict_func):
    dict_length = len(dict_func(REQUEST_URL))
    assert dict_length == 79, f"Expected length to be 79, but got {dict_length} instead"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_rus_manufactures_count(dict_func):
    rus_count = len(dict_func(REQUEST_URL)["RUSSIA"])
    assert rus_count == 22, f"Expected number of manufactures in Russia to be 22, but got {rus_count} instead"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_no_manufactures(dict_func):
    zero_count = len(dict_func(REQUEST_URL)["HONDURAS"])
    assert zero_count == 0, f"Expected that there is no manufactures in Honduras, but got {zero_count} instead"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_manufactures_count_by_name(dict_func):
    all_names = list(chain(*dict_func(REQUEST_URL).values()))
    cooper_names = []
    for name in all_names:
        if 'COOPER-STANDARD' in name:
            cooper_names.append(name)
    assert len(cooper_names) == 7, \
        f"Expected number of Cooper-Standard manufactures to be 7, but got {len(cooper_names)} instead"
