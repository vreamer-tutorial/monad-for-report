class Failure:
    def __init__(self, value, failed=False):
        self.value = value
        self.failed = failed

    def get(self):
        return self.value

    def is_failed(self):
        return self.failed

    def bind(self, f):
        if self.failed:
            return self
        try:
            x = f(self.get())
            return Failure(x)
        except:
            return Failure(None, True)
