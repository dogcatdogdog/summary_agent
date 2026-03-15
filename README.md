# 无人机任务日志总结系统 (Drone Mission Log Summarization System)

这是一个基于大语言模型（LLM）的无人机任务日志自动总结系统。它能够解析无人机飞行过程中的原始 JSON 日志数据，利用 AI 模型生成结构化的战术任务总结报告，并支持导出为 Markdown 和 Word (docx) 格式。

## 🚀 功能特性

- **日志解析**: 自动读取并解析 JSON 格式的无人机任务日志。
- **智能总结**: 集成阿里云 DashScope (通义千问) 等大模型，对复杂的任务数据进行提炼和总结。
- **多格式导出**: 支持生成 Markdown 报告，并可将其转换为专业的 Word 文档。
- **灵活配置**: 通过 `config.json` 轻松管理 API 密钥、模型选择及提示词路径。

## 🛠️ 环境要求

- **Python 版本**: 3.10
- **依赖库**: 见 `requirements.txt`

## 📦 安装步骤

1. **克隆项目**:
   ```bash
   git clone <repository_url>
   cd project
   ```

2. **创建虚拟环境 (可选但推荐)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 使用 venv\Scripts\activate
   ```

3. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ 配置说明

在使用系统前，请编辑根目录下的 `config.json` 文件：

```json
{
    "api_key": "您的 API 密钥",
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "model": "qwen-turbo",
    "prompts": {
        "purifier": "project/prompts/log_purifier.md",
        "summarizer": "project/prompts/doc_summarizer.md"
    },
    "output_dir": "project/output"
}
```

## 📂 目录结构

- `src/`: 源代码目录
  - `main.py`: 程序入口
  - `processor/`: 日志解析模块
  - `engine/`: LLM 总结核心模块
  - `exporter/`: 报告导出模块 (DOCX/MD)
- `data/`: 存放原始日志文件 (JSON)
- `prompts/`: 存放用于 LLM 的提示词模板
- `output/`: 默认的报告输出目录
- `config.json`: 系统配置文件

## 🚀 运行方法

在 `src` 目录下运行主程序：

```bash
cd src
python main.py
```

执行完成后，您可以在 `output/` 目录下找到生成的 `.md` 和 `.docx` 报告文件。

## 🧪 测试

您可以运行 `tests/test_purifier.py` 来测试日志提炼功能：

```bash
# 在项目根目录下运行
python tests/test_purifier.py
```
