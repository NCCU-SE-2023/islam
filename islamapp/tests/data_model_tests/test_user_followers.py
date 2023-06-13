import unittest
from mongoengine import connect, QuerySet
from model.data_models.user_followers import UserFollowers

# generate the unittest for the user_followers method
class TestUserFollowers(unittest.TestCase):
    def setUp(self):
        connect("islam")

    def test_create_user_followers(self):
        raw_data = {
            "scraped_ig_id": "test",
            "followers_count": 4,
            "followers_list": ["hello", "it's me", "mario", "luigi"],
            "scrape_user": "mario",
            "scraped_task_id": "202CB962AC59075B964B07152D234B40",
        }

        create_user_followers = UserFollowers.create(raw_data)
        create_user_followers = UserFollowers.create(raw_data)
        create_user_followers = UserFollowers.create(raw_data)
        self.assertIsInstance(create_user_followers, UserFollowers)

    def test_get_latest_user_followers_by_ig_id(self):
        get_latest_user_followers_by_ig_id = (
            UserFollowers.get_latest_user_followers_by_ig_id("test")
        )
        self.assertIsInstance(get_latest_user_followers_by_ig_id, UserFollowers)

    def test_get_all_user_followers_by_ig_id(self):
        get_all_user_followers_by_ig_id = UserFollowers.get_all_user_followers_by_ig_id(
            "test"
        )
        # maybe need to change the type
        self.assertIsInstance(get_all_user_followers_by_ig_id, QuerySet)

    def test_delete_user_followers_by_ig_id(self):
        delete_user_followers_by_ig_id = UserFollowers.delete_user_followers_by_ig_id(
            "test"
        )
        self.assertEqual(delete_user_followers_by_ig_id, 1)


if __name__ == "__main__":
    unittest.main()
