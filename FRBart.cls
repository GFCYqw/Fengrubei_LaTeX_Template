%%%%%%%%%%%%%%%%%%%%%%
%% start of file `FRBart.cls'.
%% 
%% Copyright 2024-2024 FRBart (3542510958@qq.com)
%% This work may be distributed and/or modified freely
%%%%%%%%%%%%%%%%%%%%%
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