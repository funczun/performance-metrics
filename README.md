# Performance Metrics

**P**erformance Metrics provides various methods for measuring the performance of code execution. Currently, it only includes time measurement, but in the future, additional performance metrics such as memory usage, CPU utilization, and more will be incorporated. This will allow for a comprehensive analysis and optimization of code performance from multiple perspectives.

## ⏱️ Timer Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func) # 원본 함수 메타데이터 유지
    
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # 시간 측정 시작
        result = func(*args, **kwargs) # 함수 실행
        end_time = time.perf_counter() # 시간 측정 종료
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.10f} seconds.") # 소수점 이하 10자리 출력
        return result

    return wrapper
```

## ⚡ Performance Measurement

**T**his decorator measures the execution time of a function. It calculates the time taken by the function to execute by recording the start and end times using Python's `time.perf_counter()` method, which provides high-resolution timing. The result is then displayed in seconds with high precision.

## 📚 How to Use

1. Download the `timer_decorator.py` file.
2. Import the `timer` module, ensuring the correct path is used.
3. Set the `repetitions` and apply as follows.
```python
from timer_decorator import timer

repetitions = 10000

@timer
def concat_using_plus():
    result = ""
    for _ in range(repetitions):
        result += "funczun"
    return result

@timer
def concat_using_join():
    result = []
    for _ in range(repetitions):
        result.append("funczun")
    return "".join(result)

if __name__ == "__main__":
    concat_using_plus()
    concat_using_join()
```
4. Run the script and compare the average execution time.
5. Confirm that `concat_using_join()` has a shorter execution time than `concat_using_plus()`.
