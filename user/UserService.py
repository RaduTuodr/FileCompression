from user.UserModel import User
from user.UserRepository import UserRepository
from user.activity.ActivityModel import Activity


def add_activity(user: User, activity: Activity):

    repository = UserRepository()
    repository.addActivity(user.get_username(), activity)
    repository.update()
