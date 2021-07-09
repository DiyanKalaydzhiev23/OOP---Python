class Task:

    def __init__(self, name, due_data):
        self.name = name
        self.due_date = due_data
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name != new_name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."

    def change_due_date(self, new_date):
        if self.due_date != new_date:
            self.due_date = new_date
            return self.due_date
        return "Date cannot be the same"

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
