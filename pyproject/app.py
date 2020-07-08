class Post:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '{}: {}'.format(self.title, self.content)

    def json(self):
        return {
                'title': self.title,
                'content': self.content,
        }


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


blog_objects = dict() # blog_name : blog_object

def create_blog_object(blogs):
    for blog in blogs:
        blog_objects[blog['title']] = Blog(blog['title'], blog['author']) # if the key dosn't exist then it adds it automatically

def add_posts_to_blog(blogs):
    for blog in blogs:
        for post in blog['posts']:
            blog_objects[blog['title']].create_post(post['title'], post['content'])

def list_all_blogs():
    counter = 1
    for key, blog in blogs.items():
        print('Blog {}: {}'.format(counter, blog))  # blog object will be printed as stated in __repr__
        counter +1


def main():

    posts_1 = [
        {
            'title': 'Post1',
            'content': 'Content Post1'
        },
        {
            'title': 'Post2',
            'content': 'Content Post2'
        },
        {
            'title': 'Post3',
            'content': 'Content Post3'
        }
    ]


    posts_2 = [
        {
            'title': 'Post1',
            'content': 'Content Post1'
        },
        {
            'title': 'Post2',
            'content': 'Content Post2'
        }
    ]

    blogs = [
        {
            'title': 'Blog1',
            'author': 'Artur',
            'posts': posts_1
        },
        {
            'title': 'Blog2',
            'author': 'Mike',
            'posts': posts_2
        }
    ]

    create_blog_object(blogs)
    add_posts_to_blog(blogs)

    for key,blog in blog_objects.items():
        print(blog)
        print(blog.posts)

    #
    # blogs[blog_title].read_all_posts()


if __name__ == '__main__':
    main()
