class Post:
    def __init__(self, message, author ):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(F"Post:{self.message} is written by author {self.author}")

