import pytest
from scholarship_awards import award_amount, is_eligible, application_status


def test_award_amount_rejects_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        award_amount("science", 90, "low", False)


def test_award_amount_rejects_negative_marks():
    with pytest.raises(ValueError, match="invalid marks"):
        award_amount("merit", -1, "low", False)


def test_award_amount_at_cutoff_is_zero():
    assert award_amount("merit", 75, "low", False) == 0


def test_merit_renewal_lowers_cutoff_and_low_income_rate():
    assert award_amount("merit", 80, "low", True) == 10 * 100


def test_sports_renewal_does_not_lower_cutoff():
    assert award_amount("sports", 64, "low", True) == 4 * 100


def test_high_income_and_large_excess_marks():
    assert award_amount("merit", 95, "high", False) == 20 * 100


def test_low_income_large_excess_marks():
    assert award_amount("merit", 95, "low", False) == 20 * 160


def test_eligibility_special_quota_backlog_boundary():
    assert is_eligible(20, 2, True) is True
    assert is_eligible(100, 3, True) is False


def test_eligibility_attendance_and_backlog_boundaries():
    assert is_eligible(74, 0, False) is False
    assert is_eligible(75, 1, False) is True
    assert is_eligible(75, 2, False) is False


def test_application_status_open_closing_and_closed():
    assert application_status(30, False, False) == "open"
    assert application_status(15, False, False) == "closing"
    assert application_status(4, False, False) == "closed"


def test_application_status_renewal_and_paper_cutoffs():
    assert application_status(40, True, False) == "open"
    assert application_status(40, False, True) == "open"
    assert application_status(25, True, True) == "closing"
