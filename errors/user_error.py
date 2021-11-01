class UserError(Exception):
    def __init(self, message: str):
        self.message = message


class IncorrectPasswordError(UserError):
    pass


class SelfAssessmentNotCompliantError(UserError):
    def __init__(self, message: str, notification: str):
        super().__init__()
        self.message = message
        self.notification = notification
