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
        <small>(Tags: {% assign ttags = post.tags | join:' | ' %}{{ ttags }})</small>
        

      </div>
    </article><hr/>
  {% endfor %}
</div>
