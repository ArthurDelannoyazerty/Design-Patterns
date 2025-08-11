import abc
import time

# ---------------------------------------------------------------------------- #
#                                 Absract Class                                #
# ---------------------------------------------------------------------------- #
class IReportGenerator(abc.ABC):
    @abc.abstractmethod
    def generate_report(self):
        pass


# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class RealReportGenerator(IReportGenerator):
    def __init__(self):
        print("RealReportGenerator: Initializing... (This is a slow process)")
        # Simulate a delay for creating this expensive object
        time.sleep(2)
        print("RealReportGenerator: Initialization complete.")

    def generate_report(self):
        print("RealReportGenerator: Generating a very sensitive and detailed financial report.")
        return "--- Financial Report ---"



class SecureReportProxy(IReportGenerator):
    def __init__(self, user: 'User'):
        self._user = user
        self._real_generator: RealReportGenerator = None

    def _check_access(self) -> bool:
        print(f"Proxy: Checking access for user '{self._user.username}'...")
        if "admin" in self._user.roles:
            print("Proxy: Access Granted.")
            return True
        else:
            print("Proxy: Access Denied. User must be an admin.")
            return False

    def generate_report(self):
        if self._check_access():
            if self._real_generator is None:
                print("Proxy: Creating the RealReportGenerator on first use.")
                self._real_generator = RealReportGenerator()
            print("Proxy: Now delegating the call to the real object.")
            return self._real_generator.generate_report()
        else:
            return "Error: You do not have permission to generate this report."


class User:
    def __init__(self, username: str, roles: list[str]):
        self.username = username
        self.roles = roles


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    admin_user = User("alice", ["admin", "viewer"])
    viewer_user = User("bob", ["viewer"])

    print("--- Scenario 1: Admin user tries to generate a report ---")
    admin_proxy = SecureReportProxy(admin_user)
    report = admin_proxy.generate_report()
    print(f"Client received: {report}\n\n")
    
    print("--- Scenario 2: Viewer user tries to generate a report ---")
    viewer_proxy = SecureReportProxy(viewer_user)
    report = viewer_proxy.generate_report()
    print(f"Client received: {report}\n")

# ---------------------------------- Output ---------------------------------- #

# --- Scenario 1: Admin user tries to generate a report ---
# Proxy: Checking access for user 'alice'...
# Proxy: Access Granted.
# Proxy: Creating the RealReportGenerator on first use.        
# RealReportGenerator: Initializing... (This is a slow process)
# RealReportGenerator: Initialization complete.
# Proxy: Now delegating the call to the real object.
# RealReportGenerator: Generating a very sensitive and detailed financial report.
# Client received: --- Financial Report ---
#
#
# --- Scenario 2: Viewer user tries to generate a report ---
# Proxy: Checking access for user 'bob'...
# Proxy: Access Denied. User must be an admin.
# Client received: Error: You do not have permission to generate this report.