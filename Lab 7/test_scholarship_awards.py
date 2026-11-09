"""Hypothesis fuzz tests and useful behavioural properties."""
from hypothesis import given, strategies as st
from scholarship_awards import parse_applicant, marks_average, payable_award

@given(st.one_of(st.text(), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_parse_applicant_arbitrary_input_does_not_crash(value):
    result = parse_applicant(value)
    assert isinstance(result, tuple) and len(result) == 2

@given(st.one_of(st.text(), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_marks_average_arbitrary_input_does_not_crash(value):
    result = marks_average(value)
    assert isinstance(result, int)
    assert result >= 0

@given(st.one_of(st.text(), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_payable_award_arbitrary_input_does_not_crash(value):
    result = payable_award(value)
    assert isinstance(result, float)
    assert result >= 0

@given(st.sampled_from(["merit", "SPORTS", " arts "]), st.integers(min_value=0, max_value=100))
def test_valid_applicant_round_trip(category, marks):
    parsed_category, parsed_marks = parse_applicant(f"{category}:{marks}")
    if category.strip():
        assert parsed_category == category.strip().title()
        assert parsed_marks == float(marks)

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=100))
def test_valid_marks_average_is_in_range(values):
    result = marks_average(",".join(map(str, values)))
    assert 0 <= result <= 100

@given(st.floats(min_value=0, max_value=1_000_000, allow_nan=False, allow_infinity=False), st.floats(min_value=0, max_value=2_000_000, allow_nan=False, allow_infinity=False))
def test_valid_payable_award_is_nonnegative(award, deduction):
    assert payable_award(f"{award}|{deduction}") >= 0
