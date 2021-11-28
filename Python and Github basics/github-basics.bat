SET repo=%1
SET directory=https://github.com/LS-Computer-Vision/
SET final=%directory%%repo%
git remote remove upstream
git remote add upstream %final%
git pull upstream main