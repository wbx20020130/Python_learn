@echo off
REM 替换为您的 GitHub 仓库地址、用户名和邮箱
set REPO_URL=https://github.com/wbx20020130/Python_learn.git
set USER_NAME=wbx20020130
set USER_EMAIL=979817025@qq.com

REM 配置 Git 用户信息
git config --global user.name "%USER_NAME%"
git config --global user.email "%USER_EMAIL%"

REM 初始化 Git 仓库（如果仓库已初始化可跳过此步）
if not exist .git (
    git init
)

REM 添加远程仓库（如果已添加可先删除再添加：git remote remove origin）
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%

REM 添加并提交所有文件
git add .
git commit -m "Initial commit"

REM 推送到 GitHub（第一次推送时可能需要输入 GitHub 账号和密码，建议配置 Git Credential Manager 或使用 SSH）
git push -u origin master
pause
