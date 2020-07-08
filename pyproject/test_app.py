import app
import unittest
from app import Post, Blog
from unittest import TestCase
from unittest.mock import patch


class PostTest(TestCase):

    def setUp(self):
        self.p = Post('Title Post','Content Post')

    def tearDown(self):
        pass

    def test_post(self):
        self.assertEqual('Title Post', self.p.title)
        self.assertEqual('Content Post', self.p.content)

    def test_json(self):
        expected = {'title': 'Title Post', 'content': 'Content Post'}
        self.assertDictEqual(expected, self.p.json())

class BlogTest(TestCase):

    def setUp(self):
        self.b1 = Blog('Test', 'Test Author')
        self.b2 = Blog('Blog', 'Artur')

    def tearDown(self):
        pass

    def test_blog(self):

        self.assertEqual('Test', self.b1.title)
        self.assertEqual('Test Author', self.b1.author)
        self.assertListEqual([], self.b1.posts)

    def test_repr_no_posts(self):

        self.assertEqual(self.b1.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(self.b2.__repr__(), 'Blog by Artur (0 posts)')

    def test_repr_many_posts(self):
        self.b1.posts = ['element']
        self.b2.posts = ['element1','element2']
        self.assertEqual(self.b1.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(self.b2.__repr__(), 'Blog by Artur (2 posts)')

    def test_read_all_posts(self):
        self.b1.posts = [
                            {
                                'title':'Post1',
                                'content': 'Content Post1'
                            }
        ]

        # self.assertEqual(len(self.b1.posts),2)

        with patch('builtins.print') as mocked_print:
            self.b1.read_all_posts()
            mocked_print.assert_called_with('Post 1: Post1, Content Post1')

            # print('Post {}: {}, {}'.format(counter, post.title, post.content))



class IntegrationTest(TestCase):

    def setUp(self):
        self.b = Blog('Test', 'Test Author')

    def tearDown(self):
        pass

    def test_create_post(self):
        self.b.create_post('Test post', 'Test content')
        self.assertEqual(len(self.b.posts),1)
        self.assertEqual(self.b.posts[0].title, 'Test post')
        self.assertEqual(self.b.posts[0].content, 'Test content')

    def test_json_with_no_posts(self):
        expected = {'title': 'Test', 'author':'Test Author', 'posts':[]}
        self.assertEqual(self.b.json(), expected)

    def test_json_for_posts(self):
        self.b.create_post('Test post', 'Test content')
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test post',
                    'content': 'Test content'
                }
            ]
        }

        self.assertDictEqual(self.b.json(), expected)

class AppTest(TestCase):

    def setUp(self):
        self.b = Blog('Test', 'Test Author')

    def tearDown(self):
        pass

    def test_list_all_blogs(self):
        app.blogs = {'Test': self.b}
        with patch('builtins.print') as mocked_print:
            app.list_all_blogs()
            mocked_print.assert_called_with('Blog 1: Test by Test Author (0 posts)')

    def test_create_blog(self):
        app.create_blog('Test','Test Author')
        self.assertEqual(str(app.blogs['Test']),str(self.b))

if __name__ == '__main__':
    unittest.main()
