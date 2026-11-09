"""Tests focused on executing every statement in scholarship_awards."""
from scholarship_awards import award_amount, is_eligible, application_status

def test_code_coverage_award_paths():
    assert award_amount("merit", 75, "low", False) == 0
    assert award_amount("merit", 80, "low", True) == 1000
    assert award_amount("sports", 64, "low", True) == 400
    assert award_amount("merit", 95, "high", False) == 2000
    assert award_amount("merit", 95, "low", False) == 3200

def test_code_coverage_eligibility_paths():
    assert is_eligible(0, 2, True)
    assert not is_eligible(100, 3, True)
    assert not is_eligible(74, 0, False)
    assert is_eligible(75, 1, False)
    assert not is_eligible(75, 2, False)

def test_code_coverage_status_paths():
    assert application_status(30, False, False) == "open"
    assert application_status(15, False, False) == "closing"
    assert application_status(4, False, False) == "closed"
    assert application_status(40, True, False) == "open"
    assert application_status(40, False, True) == "open"
    assert application_status(25, True, True) == "closing"
