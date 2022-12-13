from datetime import datetime

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d-%H-%M-%S'

    def to_python(self, value):
        return datetime.strptime(value, self.format)

    def to_url(self, value):
        return value.strftime(self.format)