<div align="right">
  语言:
    🇨🇳
  <!-- <a title="英语" href="./README.en.md">🇺🇸</a> -->
  <!-- <a title="俄语" href="../ru/README.md">🇷🇺</a> -->
</div>

# (●'◡'●)

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org) [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/) [![GitHub Release](https://img.shields.io/github/v/release/GFCYqw/Fengrubei_LaTeX_Template)](https://github.com/GFCYqw/Fengrubei_LaTeX_Template/releases/tag/v1.0.0) ![GitHub Release Date](https://img.shields.io/github/release-date/GFCYqw/Fengrubei_LaTeX_Template) ![GitHub last commit](https://img.shields.io/github/last-commit/GFCYqw/Fengrubei_LaTeX_Template) ![GitHub License](https://img.shields.io/github/license/GFCYqw/Fengrubei_LaTeX_Template)

> 北京航空航天大学“冯如杯”竞赛 `LaTeX`论文模板

[toc]

## 项目简介

这是一个北京航空航天大学“冯如杯”竞赛的 `LaTeX`论文模板。如果你是北航学子苦于冯如杯论文格式的复杂，苦于没有合适的 `LaTeX`模板，恭喜你发现了本项目。作者以为，干巴巴的模板不如一篇论文源码来的实在，所以本模板以作者获奖论文源码形式呈现，各位同学可以在直接以原论文作为参考（切忌抄袭哦）。

## 文件结构

```bash
.
├─doc	# 官方文档（包含格式要求与竞赛通知）
├─old	# 包含作者在原模板以及基础上修改后论文源代码（旧，不包含于 Release）
├─src	# 最新模板源代码
├─FRB-main.docx	# 模板导出样例（使用 Adobe Acrobat 转换为 Word，仅作为格式对照验证，文档内容有较大出入）
├─FRB-main.pdf	# 模板导出样例
├─LICENSE		# 许可证
└─README.md		# 本文档
```

## 使用方法

```bash
# （可选）下载 Release 压缩包到本地并解压缩
# 使用 git clone 克隆仓库到本地
git clone https://github.com/GFCYqw/Fengrubei_LaTeX_Template.git

# （Windows）在 src/ 目录下打开 cmd 运行快速构建脚本
.\make.bat

# 其他构建说明见 src/INSTRUCTIONS.md
```

## 更新日志

- 2024-04-07：github 项目创建（有点晚了）。
- 2024-05-19：经过提醒，发现冯如杯（fengrubei）拼错了，少个g，已修正。
- 2025-03-11：由于模板目前尚未完成（咕咕），增加了基于 [原模板](https://github.com/Hello-2073/The-Fengru-Cup-Template) 的个人修改版本（作者以此版本获三十四届创意赛道一等奖），可供各位同学参考学习 LaTeX 的使用。
- 2025-03-15：模板基本完成，重构文件结构。
- 2025-03-19：修改行距设置，使其与 Word 文档 1.5 倍行距对齐；在宏包添加了部分注释，便于学习与修改；添加了几个往届的格式要求和官方通知文件。
- 2025-03-29：修改了 `make.bat` 脚本，添加使用说明；更新参考文献格式文件，并将相关项目 `README.md` 附于 `INSTRUCTION.md` 后供参考；定义伪粗体命令临时解决“图表标题使用粗宋体”。
- 2025-03-30：规范了 `README.md` 格式标准。
- 2025-03-31：更换协议为LPPL。
- 2025-11-23：通过 WSL2 环境编译测试，使用 Windows 下 SimSun 而非 Linux 下 FandolSong 字体；修正页眉高度；将原 `FRB-style.sty` 封装为 `FRB-style.cls` 类，使用 `\documentclass{FRB-style}` 即可；更新副录标题格式修改方法为 `ctex` 接口，简化使用并统一格式。

## 待办事项

* [X] 实现图表标题编号的粗宋体
* [ ] 寻找可能的免费字体作为粗体字体
* [X] 规范原文标签命名格式

## 维护人员

* GFCYqw - *Initial work* - [GFCYqw](https://github.com/GFCYqw) - 3542510958@qq.com

## 参考致谢

* [Hello-2073/The-Fengru-Cup-Template](https://github.com/Hello-2073/The-Fengru-Cup-Template)
* [zepinglee/gbt7714-bibtex-style: GB/T 7714-2015 BibTeX Style](https://github.com/zepinglee/gbt7714-bibtex-style)

## 反馈贡献

欢迎任何人的反馈与贡献！任何问题可以打开[issue]([Issues · GFCYqw/Fengrubei_LaTeX_Template](https://github.com/GFCYqw/Fengrubei_LaTeX_Template/issues))或提交合并请求，同时欢迎各位直接与作者联系。

贡献代码时请注意：

* `git`提交请遵守 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)
* 版本化方式请遵守 [Semantic Versioning 2.0.0](https://semver.org) 规范
* 如果修改 `README.md`，请遵守 [standard-readme](https://github.com/RichardLitt/standard-readme) 规范

## 许可证

[LaTeX Project Public License 1.3c or later](LICENSE) © 2025 Martin Wilson @GFCYqw
