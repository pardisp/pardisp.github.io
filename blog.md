---
layout: default
title: Blog
---

<div class="posts">
  {% for post in site.posts %}
    <article class="post">
      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
      <div class="entry">
        {{ post.excerpt }} <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
        <p> Tags:
        <small>{% assign ttags = post.tags | join:' | ' %}</small>
        {{ ttags }} 
        </p>

      </div>
    </article><hr/>
  {% endfor %}
</div>
