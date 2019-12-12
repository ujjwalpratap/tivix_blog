project Language:- Python 3.6 , django 2.2

procedure to run the project
*** system os must be ubuntu 16 and above  ***
  some important command copy pest in terminal
    virtualenv -p python3 bog_env
    source ~/blog_env/bin/activate
  go to the project directory(tivix_blog) using cd command, ex:- cd ~/tivix_blog
    copy these command and pest it in terminal :--
      pip install -r req.txt
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver 8000
