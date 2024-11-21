import time
from functools import wraps

def timer(func):
    @wraps(func)
    
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # 시간 측정 시작
        result = func(*args, **kwargs) # 함수 실행
        end_time = time.perf_counter() # 시간 측정 종료
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.10f} seconds.")
        return result

    return wrapper