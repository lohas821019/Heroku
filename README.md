# Heroku

如何把Django post上去heroku

step 1.修改Django程式，並且要在local端可執行

step 2. >> Heroku login

step 3.啟動虛擬環境 >>.\Scripts\activate

step 4. >> git status

step 5. >> git add --all (git add .)

step 6. >> git commit-m  "First"

step 7. >> git push Heroku master

step 8. >> Heroku git: remote app(Heroku上面創的名稱)

step 9. >> heroku run bash (在heroku server上設定)

step 10. >>ls 

step 11. >>python manage.py migrate

step 12. >>python manage.py createsuperuser

##pip freeze =>requirements.txt (commit前，確認要裝的模組有沒有含在裡面)

參考資料:
https://www.youtube.com/watch?v=MoX36izzEWY&t=1590s&ab_channel=buildwithpython

https://www.796t.com/article.php?id=55206