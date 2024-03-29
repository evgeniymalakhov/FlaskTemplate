import unittest
from app.models import User, Role, Permission, AnonymousUser


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        user = User(
            email='new_test_mail@gmail.com',
            username='user1',
            password='user1')
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User(
            email='new_test_mail@gmail.com',
            username='user1',
            password='user1')
        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        user = User(
            email='new_test_mail@gmail.com',
            username='user1',
            password='cat')
        self.assertTrue(user.verify_password('user1'))
        self.assertFalse(user.verify_password('user2'))

    def test_password_salts_are_random(self):
        user = User(
            email='new_test_mail@gmail.com',
            username='user1',
            password='user1')
        user2 = User(
            email='new_test_mail2@gmail.com',
            username='user2',
            password='user1')
        self.assertTrue(user.password_hash != user2.password_hash)

    def test_roles_and_permissions(self):
        Role.insert_roles()
        user = User(
            email='new_test_mail@gmail.com',
            username='new_role_uer_test',
            password='user1')
        self.assertTrue(user.can(Permission.WRITE_ARTICLES))
        self.assertFalse(user.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        user = AnonymousUser()
        self.assertFalse(user.can(Permission.FOLLOW))
