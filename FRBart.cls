%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Start of file `FRBart.cls'.
%% Copyright 2024 M.W. (3542510958@qq.com)
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%% https://www.latex-project.org/lppl.txt
%% and version 1.3c or later is part of all distributions of LaTeX
%% version 2008 or later.
%% This work has the LPPL maintenance status `maintained'.
%% The Current Maintainer of this work is Martin Wilson.
%% This work consists of the files FRBart.cls and FRBTemplate.sty.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% % !Mode:: "TeX:UTF-8"
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{FRBart}[2024/4/8 FRB article template by GFCYqw]

\DeclareOption{12pt}{
  \PassOptionsToClass{\CurrentOption}{ctexart}
}

% 报错信息
\DeclareOption*{
  \ClassWarning{FRBart}{Unknown option '\CurrentOption' for class FRBart}
}

% 声明默认选项
\ExecuteOptions{12pt}

% 结束选项设置
\ProcessOptions\relax


% 加载基本类
\LoadClass[a4paper,12pt]{ctexart}

\RequirePackage{FRBTemplate}
\endinput
