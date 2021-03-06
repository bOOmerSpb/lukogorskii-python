import pytest
import allure
from cf_function import get_continued_fraction


@allure.feature('Continued fraction')
@allure.story('Test continued fraction')
@pytest.mark.parametrize("fraction, expected", [("239/30", [7, 1, 29]), ("256/35", [7, 3, 5, 2]), ("10/0", [])])
def test_continued_fraction(fraction, expected):
    assert get_continued_fraction(fraction) == expected
