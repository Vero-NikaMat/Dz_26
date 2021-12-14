import json


def open_file():

    with open('data/data.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)

    with open('data/comments.json', 'r', encoding='utf-8') as f:
        comments = json.load(f)

    with open('data/bookmarks.json', 'r', encoding='utf-8') as f:
        bookmarks = json.load(f)

    return posts, comments, bookmarks


def list_comments():
    """создает список из числа комментариев к каждому посту """
    posts, comments, bookmarks = open_file()
    list_count_comments = []
    for k in range(len(posts)):
        count_ = 0
        for comment in comments:
            if k+1 == comment["post_id"]:
                count_ += 1
        list_count_comments.append(count_)

    return list_count_comments


def post_and_comment():
    """добавляет в словарь поста ключ comments """
    posts, comments, bookmarks = open_file()
    list_count_comments = list_comments()
    for x, y in enumerate(posts):
        posts[x]["comments"] = list_count_comments[x]
    return posts


def comment_post_id(pk):
    """Выбираем комменты по pk"""
    posts, comments, bookmarks = open_file()
    comment_post_id = []
    for comment in comments:
        if comment["post_id"] == pk:
            comment_post_id.append(comment)

    return comment_post_id

print(comment_post_id(7))