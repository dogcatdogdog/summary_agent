import json
import os

class LogParser:
    def __init__(self, log_path: str):
        self.log_path = log_path

    def load_logs(self) -> str:
        """加载原始 JSON 日志并返回字符串格式"""
        if not os.path.exists(self.log_path):
            raise FileNotFoundError(f"找不到日志文件: {self.log_path}")
        
        with open(self.log_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 这里的目的是将结构化 JSON 转化为易于模型理解的紧凑格式
            return json.dumps(data, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    parser = LogParser("../data/mock_logs.json")
    print(parser.load_logs())
