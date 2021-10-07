---
layout: default
title: Projects
---

<ul>
    {% for project in site.data.projects.projects %}
    <li>
        <a href="{{ project.url }}">{{ project.title }}</a>
        <p>{{ project.desc }}</p>
    </li>
    {% endfor %}
</ul>
