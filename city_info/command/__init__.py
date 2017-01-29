class Command:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writes = writer

    def execute(self):
        pass

    def parse_line(self):
        pass
