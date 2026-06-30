class AlertEngine:

    def __init__(self, state_manager):
        self.state = state_manager

    def calculate_correction(self, current_close, highest_close):
        if highest_close == 0:
            return 0

        return ((highest_close - current_close) / highest_close) * 100

    def check_alerts(self, correction, levels):

        triggered = []

        for level in levels:

            if correction >= level and not self.state.is_alert_sent(level):
                triggered.append(level)

        return triggered