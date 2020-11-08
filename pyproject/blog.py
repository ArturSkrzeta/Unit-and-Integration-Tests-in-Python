from post import Post

class Blog:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []             # list of Post instances

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title, self.author, len(self.posts), 's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts] # converting each insatnce into dictionary
        }

    def read_all_posts(self):
        if len(self.posts) > 0:
            counter = 1
            for post in self.posts:
                print('Post {}: {}, {}'.format(counter, post.title, post.content))
                counter +1
