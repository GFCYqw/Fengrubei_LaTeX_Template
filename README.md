# (●'◡'●)

## Intro

这是一个北京航空航天大学“冯如杯”竞赛的 LaTeX 论文模板。如果你是北航学子苦于冯如杯论文格式的复杂，苦于没有 LaTeX 模板，恭喜你发现了本项目。

该项目包含作者参赛论文源码及重构的 LaTeX 模板，请**尽情使用与分享**，如果有使用上的问题请提 issue 或直接联系作者（联系方式见下）。同时也欢迎更多同学参与到本项目的维护中来。

干巴巴的模板不如一篇论文源码来的实在，各位同学可以在直接以原论文作为参考（切忌抄袭哦）。

官方通知和格式要求见 doc/。

## Info

- **目前版本**：2025 年，第 35 届

- **更新日期**：2025-03-29

- **贡献者**：

  - GFCYqw（3542510958@qq.com）

- **仓库内容**：

  ```bash
  .
  ├─doc	# 官方文档（包含格式要求与竞赛通知）
  ├─old	# 包含作者在原模板以及基础上修改后论文源代码（旧）
  ├─src	# 最新模板源代码
  ├─FRB-main.docx	# 模板导出样例（使用 Adobe Acrobat 转换为 Word，仅作为格式对照验证，文档内容有较大出入）
  └─FRB-main.pdf	# 模板导出样例
  ```

- **仓库地址**：https://github.com/GFCYqw/Fengrubei_LaTeX_Template.git

  ```bash
  # 使用 git clone 克隆仓库到本地
  git clone https://github.com/GFCYqw/Fengrubei_LaTeX_Template.git
  ```

- **使用方法**：

  ```bash
  # 在 src\ 目录下打开 cmd 运行
  .\make.bat
  ```
  
- **日志**：

  - 2024-04-07：github 项目创建（有点晚了）。
  - 2024-05-19：经过提醒，发现冯如杯（fengrubei）拼错了，少个g，已修正。
  - 2025-03-11：由于模板目前尚未完成（咕咕），增加了基于 [原模板](https://github.com/Hello-2073/The-Fengru-Cup-Template.git) 的个人修改版本（作者以此版本获三十四届创意赛道一等奖），可供各位同学参考学习 LaTeX 的使用。
  - 2025-03-15：模板基本完成，重构文件结构。
  - 2025-03-19：修改行距设置，使其与 Word 文档 1.5 倍行距对齐；在宏包添加了部分注释，便于学习与修改；添加了几个往届的格式要求和官方通知文件。
  - 2025-03-29：修改了 `make.bat` 脚本，添加使用说明；更新参考文献格式文件（感谢 [zepinglee/gbt7714-bibtex-style: GB/T 7714-2015 BibTeX Style](https://github.com/zepinglee/gbt7714-bibtex-style)），并将其 `README.md` 附于 `INSTRUCTION.md` 后供参考；定义伪粗体命令临时解决“图表标题使用粗宋体”。