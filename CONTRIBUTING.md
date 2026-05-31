# 🤝 贡献指南

欢迎加入我们的开源项目！无论是代码贡献、文档改进、Bug报告还是功能建议，我们都非常欢迎！

> **项目简介**：这是一个功能强大的文件批量处理工具，支持批量重命名、图片格式转换、文件压缩、分类整理、水印添加等功能，还提供AI智能助手支持自然语言操作。

---

## 📖 目录

1. [如何贡献](#1-如何贡献)
2. [开发流程](#2-开发流程)
3. [代码规范](#3-代码规范)
4. [提交指南](#4-提交指南)
5. [贡献者列表](#5-贡献者列表)

---

## 💡 快速开始

如果您是第一次贡献，可以从以下简单的任务开始：

- 📝 改进文档或示例代码
- 🐛 报告并修复简单的 Bug
- ✨ 添加小的功能改进
- 📚 补充注释和文档字符串

---

## 1. 如何贡献

### 1.1 报告问题

如果您发现了 Bug 或者有功能建议，请按照以下步骤：

1. 查看 [Issues](https://github.com/c-the-life/file_batch_tool/issues) 是否已有相关讨论
2. 如果没有，请新建一个 Issue
3. 描述清楚问题或建议：
   - 🐛 **Bug报告**：提供复现步骤、错误信息、截图
   - 💡 **功能建议**：说明您想要的功能及其用途

### 1.2 提交代码

1. **Fork 仓库**：点击 GitHub 页面右上角的 "Fork" 按钮
2. **克隆您的仓库**：
   ```bash
   git clone https://github.com/your-username/file_batch_tool.git
   cd file_batch_tool
   ```
3. **创建分支**：
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **提交更改**：按照 [提交指南](#4-提交指南) 提交
5. **推送分支**：
   ```bash
   git push origin feature/your-feature-name
   ```
6. **创建 Pull Request**：在 GitHub 上创建 PR

---

## 2. 开发流程

### 2.1 环境设置

```bash
# 克隆项目
git clone https://github.com/c-the-life/file_batch_tool.git
cd file_batch_tool

# 创建虚拟环境（推荐）
python -m venv venv
# 激活虚拟环境
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖（可选）
pip install pytest black
```

### 2.2 运行测试

```bash
# 运行测试（如果有测试文件）
pytest tests/

# 代码格式化
black src/
```

### 2.3 目录结构

```
file_batch_tool/
├── src/                    # 源代码
│   ├── core/               # 核心模块（WorkerThread）
│   ├── ui/                 # 界面模块（主窗口）
│   ├── utils/              # 工具函数（文件操作）
│   └── __init__.py         # 包导出
├── examples/               # 示例代码
├── tests/                  # 测试文件
├── screenshots/            # 截图
├── README.md               # 项目说明
├── requirements.txt         # 依赖列表
└── setup.py                # 打包配置
```

---

## 3. 代码规范

### 3.1 Python 代码规范

- 遵循 [PEP 8](https://peps.python.org/pep-0008/) 规范
- 使用 4 个空格缩进
- 行宽不超过 120 字符
- 使用类型注解
- 函数和类要有文档字符串

### 3.2 提交消息规范

```
<类型>: <简短描述>

<详细描述（可选）>
```

**类型**：
- `feat`：新功能
- `fix`：修复 Bug
- `docs`：文档更新
- `style`：代码格式（不影响功能）
- `refactor`：重构（既不新增功能也不修复 Bug）
- `test`：测试相关
- `chore`：构建/工具相关

**示例**：
```
feat: 添加图片格式转换功能

- 支持 JPG/PNG/WebP 互转
- 自动处理透明通道
```

---

## 4. 提交指南

### 4.1 基本流程

```bash
# 查看状态
git status

# 添加文件
git add .

# 提交（使用规范的提交消息）
git commit -m "feat: 添加拖拽支持"

# 拉取最新代码（避免冲突）
git pull origin master

# 推送到您的仓库
git push origin your-branch
```

### 4.2 Pull Request 规范

1. **标题**：清晰描述您的更改
2. **描述**：
   - 做了什么更改
   - 为什么做这些更改
   - 如何测试
3. **相关 Issue**：如果有相关 Issue，请引用

---

## 5. 贡献者列表

### ✨ 贡献者

感谢所有为这个项目做出贡献的人！

| 贡献者 | 贡献内容 |
|--------|----------|
| [the-life](https://github.com/c-the-life) | 项目创始人，核心功能开发 |

### 📊 贡献统计

您可以在以下页面查看详细的贡献统计：

- **GitHub**：[Contributors](https://github.com/c-the-life/file_batch_tool/graphs/contributors)
- **Gitee**：[贡献者](https://gitee.com/the-life/file_batch_tool/contributors)

### 🎖️ 贡献徽章

如果您贡献了代码，可以在您的个人资料中添加这个徽章：

```markdown
[![Contributor](https://img.shields.io/badge/Contributor-file--batch--tool-blue.svg)](https://github.com/c-the-life/file_batch_tool)
```

---

## 📝 许可证

所有贡献的代码都将遵循项目的 [MIT License](LICENSE)。

---

**再次感谢您的贡献！** 🎉
