import abc

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class MessageSender(abc.ABC):
    """The 'How'."""
    @abc.abstractmethod
    def send_message(self, subject: str, body: str):
        pass

class Notification:
    """The 'What'."""
    def __init__(self, sender: MessageSender, subject: str, body: str):
        self._sender = sender
        self.subject = subject
        self.body = body

    @abc.abstractmethod
    def send(self):
        pass

# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class EmailSender(MessageSender):
    def send_message(self, subject: str, body: str):
        print(f"Sending Email  |  SUBJECT:  {subject}  |  BODY: {body}")

class SMSSender(MessageSender):
    def send_message(self, subject: str, body: str):
        print(f"Sending SMS    |  SUBJECT:  {subject}  |  BODY: {body}")


class UrgentNotification(Notification):
    def send(self):
        urgent_subject = f"[URGENT] {self.subject}"
        print("Processing an URGENT notification...")
        self._sender.send_message(urgent_subject, self.body)

class PromotionalNotification(Notification):
    def send(self):
        promo_body = f"{self.body} --->> (To unsubscribe, reply STOP)"
        print("Processing a PROMOTIONAL notification...")
        self._sender.send_message(self.subject, promo_body)


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()

    urgent_via_email = UrgentNotification(
        sender=email_sender, 
        subject="Server Down", 
        body="The main production server is unresponsive."
    )
    urgent_via_email.send()

    urgent_via_sms = UrgentNotification(
        sender=sms_sender, 
        subject="Server Down", 
        body="The main production server is unresponsive."
    )
    urgent_via_sms.send()

    promo_via_email = PromotionalNotification(
        sender=email_sender,
        subject="Our new product is here!",
        body="Check out the amazing new Gadget Pro."
    )
    promo_via_email.send()

# ---------------------------------- Output ---------------------------------- #

# Processing an URGENT notification...
# Sending Email  |  SUBJECT:  [URGENT] Server Down  |  BODY: The main production server is unresponsive.
# Processing an URGENT notification...
# Sending SMS    |  SUBJECT:  [URGENT] Server Down  |  BODY: The main production server is unresponsive.
# Processing a PROMOTIONAL notification...
# Sending Email  |  SUBJECT:  Our new product is here!  |  BODY: Check out the amazing new Gadget Pro. --->> (To unsubscribe, reply STOP)