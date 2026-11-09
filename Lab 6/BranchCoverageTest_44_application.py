"""Tests explicitly exercise both outcomes of each decision branch."""
import pytest
from scholarship_awards import award_amount, is_eligible, application_status

def test_category_and_marks_validation_branches():
    with pytest.raises(ValueError): award_amount("other", 90, "low", False)
    with pytest.raises(ValueError): award_amount("merit", -1, "low", False)

def test_award_cutoff_renewal_income_and_excess_branches():
    assert award_amount("merit", 75, "low", False) == 0
    assert award_amount("merit", 80, "low", True) == 1000
    assert award_amount("sports", 64, "low", True) == 400
    assert award_amount("merit", 95, "high", False) == 2000
    assert award_amount("merit", 95, "low", False) == 3200

def test_eligibility_all_decisions():
    assert is_eligible(0, 2, True) is True
    assert is_eligible(100, 3, True) is False
    assert is_eligible(74, 0, False) is False
    assert is_eligible(75, 1, False) is True
    assert is_eligible(75, 2, False) is False

def test_status_all_decisions_and_cutoffs():
    assert application_status(30, False, False) == "open"
    assert application_status(15, False, False) == "closing"
    assert application_status(4, False, False) == "closed"
    assert application_status(40, True, False) == "open"
    assert application_status(40, False, True) == "open"
    assert application_status(25, True, True) == "closing"
