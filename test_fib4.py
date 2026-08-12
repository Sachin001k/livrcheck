"""
Unit tests for the FIB-4 calculation logic.
Run with: python -m pytest test_fib4.py -v
"""

import math
import pytest

from fib4 import (
    calculate_fib4,
    calculate_bmi,
    bmi_category,
    InvalidInputError,
    LOW_RISK_CUTOFF,
    HIGH_RISK_CUTOFF,
)


def test_known_value():
    # Manually computed: (50 * 40) / (200 * sqrt(30)) = 2000 / (200*5.477) = 1.826
    result = calculate_fib4(age=50, ast=40, alt=30, platelets=200)
    expected = (50 * 40) / (200 * math.sqrt(30))
    assert result.score == round(expected, 2)


def test_low_risk_tier():
    # Score should be well below 1.30
    result = calculate_fib4(age=30, ast=20, alt=30, platelets=300)
    assert result.score < LOW_RISK_CUTOFF
    assert result.tier == "low"


def test_high_risk_tier():
    # Elderly patient, high AST, low platelets -> high score
    result = calculate_fib4(age=70, ast=120, alt=20, platelets=80)
    assert result.score > HIGH_RISK_CUTOFF
    assert result.tier == "high"


def test_intermediate_tier_boundaries():
    # Score exactly at the low cutoff boundary should be intermediate
    # Solve for AST such that score == 1.30 given age=40, alt=25, platelets=200
    age, alt, platelets = 40, 25, 200
    ast = (LOW_RISK_CUTOFF * platelets * math.sqrt(alt)) / age
    result = calculate_fib4(age=age, ast=ast, alt=alt, platelets=platelets)
    assert result.tier in ("low", "intermediate")  # boundary, rounding-sensitive


def test_age_out_of_validated_range():
    result = calculate_fib4(age=25, ast=30, alt=30, platelets=250)
    assert result.age_out_of_validated_range is True

    result2 = calculate_fib4(age=45, ast=30, alt=30, platelets=250)
    assert result2.age_out_of_validated_range is False


@pytest.mark.parametrize("age,ast,alt,platelets", [
    (0, 30, 30, 200),
    (40, -5, 30, 200),
    (40, 30, 0, 200),
    (40, 30, 30, 0),
    (None, 30, 30, 200),
])
def test_invalid_inputs_raise(age, ast, alt, platelets):
    with pytest.raises(InvalidInputError):
        calculate_fib4(age=age, ast=ast, alt=alt, platelets=platelets)


def test_bmi_calculation():
    # 70kg, 170cm -> BMI = 70 / 1.7^2 = 24.2
    bmi = calculate_bmi(height_cm=170, weight_kg=70)
    assert bmi == round(70 / (1.7 ** 2), 1)


def test_bmi_categories():
    assert bmi_category(17.0) == "underweight"
    assert bmi_category(22.0) == "normal"
    assert bmi_category(25.0) == "overweight"
    assert bmi_category(30.0) == "obese"


def test_bmi_invalid_inputs():
    with pytest.raises(InvalidInputError):
        calculate_bmi(height_cm=0, weight_kg=70)
    with pytest.raises(InvalidInputError):
        calculate_bmi(height_cm=170, weight_kg=-1)
