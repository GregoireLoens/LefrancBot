

def prevent_concurrent(lock):
    """
        This decorator is made to ensure no conccurent sqlite operations overlap
        and result in a "database locked" error.
    """
    def prevent_concurrent_decorator(func):
        def function_wrapper(*args, **kwargs):
            lock.acquire()
            ret = func(*args, **kwargs)
            lock.release()
            return ret

        return function_wrapper
    
    return prevent_concurrent_decorator