from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):
    """
            class that represent the user in the system
            extended the django user module

    """
    def __str__(self):
        return "@{}".format(self.username)

