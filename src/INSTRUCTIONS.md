主文档为 FRB-main.tex，使用 XeLaTeX 编译

可以使用 make.bat 构建（Windows），此脚本将会拷贝一份 pdf 至上级文件夹

可将各章节拆分至 chap/ 后 input 进主文档

```bash
# 文件结构
src
├─code	# 代码
├─fonts	# 字体
├─img	# 插图
├─FRB-main.tex	# 主文档
├─FRB-style.sty	# 模板宏包
├─FRB-ref.bib	# 参考文献库
├─gbt7714.sty	# gbt-7714 参考文献格式
├─gbt7714-author-year.bst
├─gbt7714-numerical.bst
├─make.bat	# 构建脚本
└─INSTRUCTIONS.md	# 本指南
```

