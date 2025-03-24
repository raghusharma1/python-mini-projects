import pytest
from calculate import month_days

class Test_CalculateMonthDays:

    @pytest.mark.parametrize("month, leap_year, expected", [(1, True, 31), (1, False, 31)])
    def test_January_days(self, month, leap_year, expected):
        assert month_days(month, leap_year) == expected

    @pytest.mark.parametrize("month, leap_year, expected", [(2, True, 29)])
    def test_February_days_leap_year(self, month, leap_year, expected):
        assert month_days(month, leap_year) == expected

    @pytest.mark.parametrize("month, leap_year, expected", [(2, False, 28)])
    def test_February_days_nonleap_year(self, month, leap_year, expected):
        assert month_days(month, leap_year) == expected

    @pytest.mark.parametrize("month, leap_year, expected", [(4, True, 30), (4, False, 30)])
    def test_April_days(self, month, leap_year, expected):
        assert month_days(month, leap_year) == expected

    @pytest.mark.parametrize("month, leap_year, expected", [(12, True, 31), (12, False, 31)])
    def test_December_days(self, month, leap_year, expected):
        assert month_days(month, leap_year) == expected

    @pytest.mark.parametrize("month, leap_year", [(13, True), (-1, False)])
    def test_invalid_month(self, month, leap_year):
        with pytest.raises(ValueError):
            month_days(month, leap_year)
