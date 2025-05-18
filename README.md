# 🗂️ 文件整理工具（Desktop Organizer）

这是一个基于 Python 编写的桌面文件整理工具。它可以自动将指定目录下的文件根据类型归类到不同的子文件夹中（如 Excel、Word、图片、视频等），并记录每一次操作的日志，适合办公桌面快速整理、提升效率。

## 📌 功能特点

- 支持多种文件类型的自动分类整理
- 自动创建对应文件夹（如 Word、PDF、Image 等）
- 日志记录操作过程，便于追踪
- 操作错误时自动记录错误日志
- 脚本路径与日志文件分离，便于部署

## 🛠 支持的文件类型

| 类型         | 扩展名示例                                       |
|--------------|------------------------------------------------|
| Excel        | `.xlsx`, `.xls`, `.xlsm` 等                     |
| Word         | `.docx`, `.doc`, `.dotx` 等                     |
| PowerPoint   | `.pptx`, `.ppt`, `.ppsx` 等                     |
| PDF          | `.pdf`                                         |
| 图片（Image） | `.jpg`, `.png`, `.gif`, `.webp` 等              |
| 视频（Video） | `.mp4`, `.avi`, `.mkv` 等                       |
| 音频（Audio） | `.mp3`, `.wav`, `.flac` 等                      |
| 文本（Text）  | `.txt`, `.md`, `.log` 等                        |
| 编程文件     | `.py`, `.js`, `.html`, `.css`, `.xml` 等        |
| 压缩文件     | `.zip`, `.rar`, `.tar`, `.gz` 等                |

## 🚀 快速开始

### 1. 克隆本仓库

```bash
git clone https://github.com/你的用户名/文件整理工具.git
cd 文件整理工具
