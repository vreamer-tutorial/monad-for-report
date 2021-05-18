class Failure:
    def __init__(self, value, errors=[]):
        self.value = value
        self.errors = errors

    def get(self):
        return self.value

    def get_errors(self):
        return self.errors

    def is_failed(self):
        return len(self.errors) > 0

    def __or__(self, f):
        return self.bind(f)

    def bind(self, f):
        if self.is_failed():
            return self
        try:
            x = f(self.get())
            return Failure(x)
        except Exception as e:
            return Failure(None, [str(e)])
