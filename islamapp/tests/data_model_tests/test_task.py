import time
import unittest
from mongoengine import connect, QuerySet
from model.task import Task


# generate the unittest for the user_followers method
class TestTask(unittest.TestCase):
    def setUp(self):
        connect("islam")
        self.test_task = Task.create_task(
            "test_user", "FOLLOWERS", {"test_detail": "test_detail"}
        )

    def test_create_task(self):
        create_task = Task.create_task(
            "test_user", "FOLLOWERS", {"test_detail": "test_detail"}
        )
        self.assertIsInstance(create_task, Task)

    def test_set_status(self):
        self.test_task.set_status("ERROR")
        self.assertEqual(self.test_task.status, "ERROR")

    def test_set_error_msg(self):
        self.test_task.set_error_msg({"error msg": "test error msg"})
        self.assertEqual(self.test_task.error_msg, {"error msg": "test error msg"})

    def test_set_start_time(self):
        self.test_task.retry_task()
        self.assertEqual(self.test_task.retry_times, 1)

    def test_get_by_status(self):
        get_by_status = Task.get_by_status("ERROR")
        self.assertIsInstance(get_by_status, QuerySet)

    def test_get_by_create_user(self):
        get_by_create_user = Task.get_by_create_user("test_user")
        self.assertIsInstance(get_by_create_user, QuerySet)

    def test_get_by_id(self):
        get_by_id = Task.get_by_id(self.test_task.task_id)
        self.assertIsInstance(get_by_id, Task)


if __name__ == "__main__":
    unittest.main()
