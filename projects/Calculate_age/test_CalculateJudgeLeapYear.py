import pytest
import time
from calendar import isleap
from calculate import judge_leap_year

class Test_CalculateJudgeLeapYear():
    @pytest.mark.positive
    def test_judge_leap_year_known(self):
        # Arrange
        known_leap_year = 2000

        # Act
        result = judge_leap_year(known_leap_year)

        # Assert
        assert result is True

    @pytest.mark.negative
    def test_judge_leap_year_non_leap_year(self):
        # Arrange
        known_non_leap_year = 2001

        # Act
        result = judge_leap_year(known_non_leap_year)

        # Assert
        assert result is False

    @pytest.mark.positive
    def test_judge_leap_year_exceptional_year(self):
        # Arrange
        exceptional_century_year = 2000

        # Act
        result = judge_leap_year(exceptional_century_year)

        # Assert
        assert result is True

    @pytest.mark.negative
    def test_judge_leap_year_typical_century_year(self):
        # Arrange
        typical_century_year = 1900

        # Act
        result = judge_leap_year(typical_century_year)

        # Assert
        assert result is False
