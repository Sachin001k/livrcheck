"""
Core FIB-4 calculation logic for LivrCheck.

Formula source: Sterling RK, Lissen E, Clumeck N, et al. Development of a
simple noninvasive index to predict significant fibrosis in patients with
HIV/HCV coinfection. Hepatology. 2006;43(6):1317-1325.

    FIB-4 = (Age * AST) / (Platelets * sqrt(ALT))

Where:
    Age       = years
    AST       = U/L (also called SGOT)
    ALT       = U/L (also called SGPT)
    Platelets = x10^9/L

Risk tiers used here follow the widely cited cut-offs:
    < 1.30            -> Low risk        (NPV ~90.7% for advanced fibrosis)
    1.30 - 3.25        -> Intermediate risk
    > 3.25            -> High risk       (97% specificity for advanced fibrosis)

These cut-offs, and FIB-4 generally, are validated primarily for adults aged
35-65. Outside that range the score should be treated with extra caution.
"""

import math
from dataclasses import dataclass


LOW_RISK_CUTOFF = 1.30
HIGH_RISK_CUTOFF = 3.25

VALIDATED_AGE_MIN = 35
VALIDATED_AGE_MAX = 65


class InvalidInputError(ValueError):
    """Raised when inputs to the FIB-4 calculation are invalid."""


@dataclass
class Fib4Result:
    score: float
    tier: str  # "low" | "intermediate" | "high"
    age_out_of_validated_range: bool


def calculate_fib4(age: float, ast: float, alt: float, platelets: float) -> Fib4Result:
    """
    Calculate the FIB-4 score and risk tier.

    Raises InvalidInputError if any input is non-positive or ALT is zero
    (which would cause division by zero) or if platelets is zero.
    """
    for name, value in (("age", age), ("AST", ast), ("ALT", alt), ("platelets", platelets)):
        if value is None:
            raise InvalidInputError(f"{name} is required.")
        if value <= 0:
            raise InvalidInputError(f"{name} must be a positive number.")

    score = (age * ast) / (platelets * math.sqrt(alt))
    score = round(score, 2)

    if score < LOW_RISK_CUTOFF:
        tier = "low"
    elif score <= HIGH_RISK_CUTOFF:
        tier = "intermediate"
    else:
        tier = "high"

    age_out_of_range = not (VALIDATED_AGE_MIN <= age <= VALIDATED_AGE_MAX)

    return Fib4Result(score=score, tier=tier, age_out_of_validated_range=age_out_of_range)


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """Calculate BMI (kg/m^2) from height in cm and weight in kg."""
    if height_cm is None or weight_kg is None:
        raise InvalidInputError("Height and weight are required.")
    if height_cm <= 0 or weight_kg <= 0:
        raise InvalidInputError("Height and weight must be positive numbers.")
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def bmi_category(bmi: float) -> str:
    """
    Categorize BMI using thresholds commonly used for Asian populations,
    which are lower than the standard WHO thresholds (Asian populations
    show elevated metabolic risk at lower BMI values).
    """
    if bmi < 18.5:
        return "underweight"
    elif bmi < 23.0:
        return "normal"
    elif bmi < 27.5:
        return "overweight"
    else:
        return "obese"
