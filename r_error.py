class r_error(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    def __repr__(self):
        return [code, msg]