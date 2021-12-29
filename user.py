class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_tittle = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_tittle(self, new_job_tittle):
        self.current_job_tittle = new_job_tittle

    def get_user_info(self):
        print(
            f"User {self.name} currently works as a {self.current_job_tittle}. you can contact by {self.email}"
        )

