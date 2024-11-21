import time

# 반복할 횟수 설정
repetitions = 1000

# 실행할 코드 설정
def code_to_execute():
    temp = 0

# 성능 측정 시작
start_time = time.perf_counter()

# 코드 반복 실행
for _ in range(repetitions):
    code_to_execute()

# 성능 측정 종료
end_time = time.perf_counter()

# 평균 실행 시간 계산
average_time = (end_time - start_time) / repetitions

# 결과 출력
print(f"Average Execution Time: {average_time:.10f} seconds")