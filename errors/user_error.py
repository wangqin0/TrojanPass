class UserError(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


class IncorrectPasswordError(UserError):
    def __init__(self, message: str, net_id: str):
        super().__init__(message)
        self.net_id = net_id


class SelfAssessmentNotCompliantError(UserError):
    def __init__(self, message: str, notification: str):
        super().__init__(message)
        self.notification = notification
