import os
import datetime
from processor.log_parser import LogParser
from engine.summarizer import MissionSummarizer
from exporter.docx_builder import DocxBuilder

def main():
    # 1. 初始化路径与配置
    log_file = "../data/mock_logs.json"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_docx = f"../output/Mission_Summary_{timestamp}.docx"
    
    print("🚀 无人机任务日志总结系统启动...")
    print(f"📂 输入日志: {log_file}")

    try:
        # 2. 解析日志
        parser = LogParser(log_file)
        raw_logs_str = parser.load_logs()
        
        # 3. LLM 处理
        summarizer = MissionSummarizer()
        final_md_report = summarizer.process(raw_logs_str)
        
        if not final_md_report or "失败" in final_md_report:
            print("❌ 报告生成中止。")
            return

        # 4. 导出 Markdown (新增：保存中间过程)
        md_output_path = output_docx.replace(".docx", ".md")
        with open(md_output_path, "w", encoding="utf-8") as f:
            f.write(final_md_report)
        print(f"📝 中间过程 Markdown 已保存: {md_output_path}")

        # # 5. 导出 Word
        # builder = DocxBuilder(output_docx)
        # builder.save_report(final_md_report)
        
        # print(f"\n✨ 任务圆满完成！报告已保存在: {output_docx}")

    except Exception as e:
        print(f"💥 系统运行出错: {e}")

if __name__ == "__main__":
    main()
