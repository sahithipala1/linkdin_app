from user import User
from post import Post

app_user_one = User("sahi@gmail.com", "sahi", "pass", "Developer")
app_user_one.get_user_info()

app_user_two = User("ram@gmail.com", "ram", "vo", "engineer")
app_user_two.get_user_info()

app_user_one.change_password("lulu")
app_user_one.get_user_info()

post_one = Post("do or die", app_user_two.name)
post_one.get_post_info()


