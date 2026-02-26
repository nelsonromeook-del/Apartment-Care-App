from datetime import datetime

def log_event(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open("activity.log", "a") as log:
                log.write(f"[{datetime.now()}] {action}\n")
            return result
        return wrapper
    return decorator