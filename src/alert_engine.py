def check_alerts(correction: float, levels: list, triggered: list):
    """
    Returns newly triggered alert levels based on correction percentage.

    Args:
        correction: current drawdown percentage
        levels: configured alert thresholds (e.g. [5, 10, 15])
        triggered: already triggered levels

    Returns:
        list of newly triggered levels
    """

    new_alerts = []

    for level in levels:
        if correction >= level and level not in triggered:
            new_alerts.append(level)

    return new_alerts