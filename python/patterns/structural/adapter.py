import abc
import json

class LegacyAnalytics:
    """The Adaptee: A third-party library with an incompatible interface"""
    def send_analytic_log(self, log_type: str, log_data_json: str):
        print("LegacyAnalytics: Sending log...")
        print(f"  - Log Type: {log_type}")
        print(f"  - Log Data: {log_data_json}")


class IAnalyticsService(abc.ABC):
    @abc.abstractmethod
    def track_event(self, event_name: str, user_id: int):
        pass


class AnalyticsAdapter:
    def __init__(self, legacy_analytics_service: LegacyAnalytics):
        self._legacy_service = legacy_analytics_service

    def track_event(self, event_name: str, user_id: int):
        print("Adapter: Converting a 'track_event' call to a 'send_analytic_log' call.")
        # 1. Translate the data into the format the Adaptee expects (a JSON string)
        log_data = {"event": event_name, "user": user_id}
        log_data_json = json.dumps(log_data)
        
        # 2. Call the Adaptee's method with the translated data
        self._legacy_service.send_analytic_log("USER_EVENT", log_data_json)



# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    legacy_service = LegacyAnalytics()
    
    adapter = AnalyticsAdapter(legacy_service)
    print("\nClient: Executing business logic and tracking an event.")
    adapter.track_event("UserLoggedIn", 12345)

# ---------------------------------- Output ---------------------------------- #

# Client: Executing business logic and tracking an event.
# Adapter: Converting a 'track_event' call to a 'send_analytic_log' call.
# LegacyAnalytics: Sending log...
#   - Log Type: USER_EVENT
#   - Log Data: {"event": "UserLoggedIn", "user": 12345}