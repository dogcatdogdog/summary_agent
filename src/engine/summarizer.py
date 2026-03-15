import json
import os
import re
from openai import OpenAI

class MissionSummarizer:
    def __init__(self, config_path: str = "../config.json"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        self.client = OpenAI(
            api_key=self.config["api_key"],
            base_url=self.config["base_url"]
        )
        self.model = self.config["model"]

    def _load_prompt(self, prompt_key: str) -> str:
        prompt_path = self.config["prompts"][prompt_key]
        if prompt_path.startswith("project/"):
            prompt_path = "../" + prompt_path.split("/", 1)[1]
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"找不到提示词文件: {prompt_path}")
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    def _call_llm(self, system_prompt: str, user_input: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.1
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"❌ LLM 调用失败: {e}")
            return ""

    def process(self, raw_logs: str) -> str:
        """单阶段处理：原始日志 -> 报告生成"""
        # 直接使用 doc_summarizer 提示词，并将 {raw_log_data} 替换为原始 JSON
        summarizer_prompt = self._load_prompt("summarizer").replace("{raw_log_data}", raw_logs)
        print("⏳ 正在直接从原始日志解析并生成战术总结报告...")
        report_md = self._call_llm(summarizer_prompt, "请基于原始数据生成结构化战术报告")
        
        return report_md

if __name__ == "__main__":
    import sys
    import os
    # 添加 src 目录到 path，这样可以直接从 processor 导入
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from processor.log_parser import LogParser
    parser = LogParser("../data/mock_logs.json")
    raw_logs = parser.load_logs()
    
    engine = MissionSummarizer()
    print(engine.process(raw_logs))
