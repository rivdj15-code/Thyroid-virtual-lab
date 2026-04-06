def interpret_thyroid(TSH, T3, T4):
    if TSH > 4.0 and T3 < 80 and T4 < 5.0:
        return "Hypothyroidism"
    elif TSH < 0.4 and T3 > 200 and T4 > 12.0:
        return "Hyperthyroidism"
    elif 0.4 <= TSH <= 4.0:
        return "Normal (Euthyroid)"
    else:
        return "Subclinical / Borderline - Further testing needed"
