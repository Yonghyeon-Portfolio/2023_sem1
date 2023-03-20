git status
git pull
git add .
echo "commit message: "
read commitMsg
git commit -m "$commitMsg"
git push