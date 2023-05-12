import unittest
from mongoengine import connect,QuerySet
from model.data_models.user_following import UserFollowing

#generate the unittest for the user_following method
class TestUserFollowing(unittest.TestCase):
    
    def setUp(self):
        connect('islam')        
    
    def test_create_user_following(self):
        raw_data = {
            "scraped_ig_id": "test",
            "following_count": 4,
            "following_list": ["hello","it's me","mario","luigi"],
            "scrape_user": "mario",
            "scraped_task_id": "202CB962AC59075B964B07152D234B40",
        }
        
        create_user_following = UserFollowing.create_user_following(raw_data)
        self.assertIsInstance(create_user_following, UserFollowing)
        
    def test_get_latest_user_following_by_ig_id(self):
        get_latest_user_following_by_ig_id = UserFollowing.get_latest_user_following_by_ig_id("test")
        self.assertIsInstance(get_latest_user_following_by_ig_id, UserFollowing)
        
    def test_get_all_user_following_by_ig_id(self):
        get_all_user_following_by_ig_id = UserFollowing.get_all_user_following_by_ig_id("test123")
        print(get_all_user_following_by_ig_id)
        # maybe need to change the type
        self.assertIsInstance(get_all_user_following_by_ig_id, QuerySet)
    
    def test_delete_user_following_by_ig_id(self):
        delete_user_following_by_ig_id = UserFollowing.delete_user_following_by_ig_id("test")
        self.assertEqual(delete_user_following_by_ig_id, 1)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestUserFollowing('test_get_latest_user_following_by_ig_id'))
    # suite.addTest(TestUserFollowing('test_create_user_following_change'))
    # suite.addTest(TestUserFollowing('test_delete_user_following_by_ig_id'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())



