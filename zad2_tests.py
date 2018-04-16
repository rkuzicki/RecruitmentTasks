import unittest
from zad2 import get_user_posts, get_duplicate_posts, get_closest_neighbor, get_distances


class TestJsonMethods(unittest.TestCase):

    # few structures created to immitate JSONs used in this exercise
    posts = [{'userId': 1, 'title': 'title1'},
             {'userId': 2, 'title': 'title2'},
             {'userId': 2, 'title': 'title1'}]
    users = [{'id': 1,  'username': 'Bret',  'address': {'geo': {'lat': '37.3159', 'lng': '81.1496'}}},
             {'id': 2, 'username': 'Calo', 'address': {'geo': {'lat': '1.0', 'lng': '15.15'}}},
             {'id': 3, 'username': 'Calos', 'address': {'geo': {'lat': '-0.1', 'lng': '10.3'}}}]
    users_wrong = [{'id': 1,  'usesrname': 'Bret',  'address': {'geo': {'lat': '37.3159', 'lng': '81.1496'}}},
                   {'id': 2, 'username': 'Calo', 'address': {'geo': {'lat': '1.0', 'lng': '15.15'}}},
                   {'id': 3, 'username': 'Calos', 'address': {'geo': {'lat': '-0.1', 'lng': '10.3'}}}]
    posts_wrong = [{'userId': 1, 'titlek': 'title1'},
                   {'userId': 2, 'title': 'title2'},
                   {'userId': 2, 'title': 'title1'}]

    def test_user_posts(self):
        res_array = ["User Bret napisal 1 postow.", "User Calo napisal 2 postow.", "User Calos napisal 0 postow."]
        self.assertEqual(get_user_posts(self.users, self.posts), res_array)
        self.assertEqual(get_user_posts([], []), [])
        self.assertEqual(get_user_posts(self.users_wrong, self.posts), [])

    def test_duplicate_posts(self):
        self.assertEqual(get_duplicate_posts(self.posts), ['title1'])
        self.assertEqual(get_duplicate_posts(self.posts_wrong), [])

    def test_closest_neighbor(self):
        self.assertEqual(get_closest_neighbor("Bret", 37.3159, 81.1496, self.users), "Calo")
        self.assertEqual(get_closest_neighbor("Calo", 1.0, 15.15, self.users), "Calos")
        with self.assertRaises(KeyError):
            get_closest_neighbor("Calo", self.users[1]["latt"], 11.11, self.users)
            get_closest_neighbor("Calo", 1.0, 15.15, self.users_wrong)

    def test_get_distances(self):
        distance_dict = {'Bret': 'Calo', 'Calo': 'Calos', 'Calos': 'Calo'}
        self.assertEqual(get_distances(self.users), distance_dict)
        self.assertEqual(get_distances([]), {})
        self.assertEqual(get_distances(self.users_wrong), {})


if __name__ == '__main__':
    unittest.main()
