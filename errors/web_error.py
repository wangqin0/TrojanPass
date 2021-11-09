class WebError(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


class UnexpectedUrlError(WebError):
    def __init__(self, message: str, url: str, image_name: str):
        super().__init__(message)
        self.url = url
        self.image_name = image_name
