random_name=$(od  -An -N4 -tu8 < /dev/urandom | xargs)
random_name="trojan-pass-${random_name}"

echo "Try to create heroku project $random_name"

heroku create "${random_name}"
heroku git:remote -a "${random_name}"

heroku buildpacks:set heroku/python
heroku addons:create scheduler:standard
heroku config:set PATH=/usr/local/bin:/usr/bin:/bin:/app/vendor/:/app/vendor/firefox/:/app/vendor/geckodriver
heroku buildpacks:add https://github.com/ronnielivingsince1994/heroku-integrated-firefox-geckodriver

echo "
What you need to do next - run the following command:
heroku config:set TROJAN_PASS_NETID=<Your Net ID>
heroku config:set TROJAN_PASS_PASSWORD=<Your NetID password>
heroku config:set TROJAN_PASS_GMAIL_ACCOUNT=<Your Gmail Account>
heroku config:set TROJAN_PASS_GMAIL_PASSWORD=<Your Gmail Password>
git add . && git commit -m "trigger deploy" && git push heroku main
"
