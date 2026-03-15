import os
import json
from project.src.processor.log_parser import LogParser
from project.src.engine.summarizer import MissionSummarizer

def test_purifier():
    print("🔍 开始测试 Log Purifier (日志提炼) 阶段...")
    
    # 1. 加载配置与数据
    log_file = "project/data/mock_logs.json"
    output_path = "project/output/purified_facts_test.md"
    
    parser = LogParser(log_file)
    raw_logs = parser.load_logs()
    
    # 2. 初始化引擎并仅执行第一阶段（提炼）
    summarizer = MissionSummarizer()
    
    # 获取提炼用的 Prompt
    purifier_prompt = summarizer._load_prompt("purifier").replace("{raw_log_data}", raw_logs)
    
    print("⏳ 正在请求 LLM 进行事实提炼...")
    purified_facts = summarizer._call_llm(purifier_prompt, "请开始事实提炼")
    
    if purified_facts:
        # 3. 保存结果
        os.makedirs("project/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(purified_facts)
        
        print(f"✅ 提炼完成！结果已保存至: {output_path}")
        print("\n--- 提炼内容预览 ---")
        print(purified_facts)
        print("------------------")
    else:
        print("❌ 提炼失败。")

if __name__ == "__main__":
    # 确保 PYTHONPATH 包含项目根目录
    test_purifier()
