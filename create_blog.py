import sys, os, re

os.system("rm -rf blog && mkdir blog")

with open('blog_layout.html', 'r') as f:
  layout = f.read()

placeholder_text = '[THE_PLACEHOLDER_FOR_BLOG_LAYOUT]'

def get_title(content):
    pattern = r'<title>(.*?)</title>'
    return re.findall(pattern, content, re.DOTALL)[0]

def get_body(content):
    pattern = r'<post>(.*?)</post>'
    return re.findall(pattern, content, re.DOTALL)[0]

titles_list = ""
for post in sorted(os.listdir('_posts'), reverse=True):
    if not post.startswith('post'):
        continue
    with open('_posts/'+post, 'r') as f:
        post_content = f.read()
        title = get_title(post_content)
        body = get_body(post_content)
        print(f"reading {post}")
    with open(f'blog/{post}', 'w') as f:
        f.write(layout.replace(placeholder_text, body))

    titles_list += f"<p><a href=\"blog/{post}\">{title}</a></p>" + '\n\n'

with open('blog.html', 'w') as f:
    f.write(layout.replace(placeholder_text, titles_list))
    f.write('\n')
