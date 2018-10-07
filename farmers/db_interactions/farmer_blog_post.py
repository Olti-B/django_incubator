from farmers.db_farmers.farmes_regiser_model import PostProduct


class RetriveAllPostByFarmer:
    _email = None

    def __init__(self, email=''):
        self._email = email
        pass

    def get_all_post_made_by_user(self):
        post_made = PostProduct.objects.filter(email=self._email)
        return post_made
