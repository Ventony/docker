import os
from flask import Flask

app = Flask(__name__)

# 데이터 디렉토리 경로 설정
data_dir = '/app/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

@app.route('/')
def hello():
    with open(f'{data_dir}/app_log.txt', 'a') as log_file:
        log_file.write("New request logged.\n")
    return "안녕하세요! 여기는 API 서버입니다."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
