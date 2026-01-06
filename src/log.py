from flask.views import MethodView

# TODO: update log page when everytime something happens
class Log(MethodView):
    
    def __init__(self, lg):
        super().__init__()
        
        self.log_stream = lg
        
    def set_log_stream(self, lg):
        self.log_stream = lg
        
    def get(self):
        log_content = self.log_stream.getvalue()
        return f"<h3>Logs of the system:</h3><pre>{log_content}</pre>"
    
    