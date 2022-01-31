import sys, os

with open('blog_layout.html', 'r') as f:
  layout = f.read()

placeholder_text = '[THE_PLACEHOLDER_FOR_BLOG_LAYOUT]'

blog_content = ""
for post in sorted(os.listdir('_posts'), reverse=True):
    if not post.startswith('post'):
        continue
    with open('_posts/'+post, 'r') as f:
        post_content = f.read()

    blog_content += post_content + '\n\n'

layout = layout.replace(placeholder_text, blog_content)
with open('blog.html', 'w') as f:
    f.write(layout)
    f.write('\n')
