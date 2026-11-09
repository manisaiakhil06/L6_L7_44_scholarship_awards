# Lab 7 — Fuzz Testing

This lab uses Hypothesis to fuzz the three scholarship-record input functions. Malformed inputs are handled defensively with stable default values: `("", 0.0)` for applicant parsing, `0` for averages, and `0.0` for payable awards. Valid inputs retain the expected parsing and award calculation behaviour.

## Run

```bash
python -m pip install pytest hypothesis
python scholarship_awards.py
python -m pytest -q test_scholarship_awards.py
```

Hypothesis generates arbitrary values and checks that the functions do not crash, while additional properties check valid-input ranges and nonnegative award results.
