def format_duration(seconds):
    if not seconds:
        return "now"
    result = []

    units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]

    for unit, value in units:
        unit_value, seconds = divmod(seconds, value)
        if unit_value:
            result.append(str(unit_value) + f" {unit}{'s' if unit_value > 1 else ''}")

    if len(result) >= 2:
        return ", ".join(result[:-1]) + " and " + result[-1]
    return result[0]