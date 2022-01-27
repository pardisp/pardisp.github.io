---
layout: default
title: Publications
---

<ul>
    {% for publication in site.data.publications.pubs %}
    <li>
        <p><b>{{ publication.title }}</b>.<br/>
            {{ publication.authors }}.<br/>
            <i>{{ publication.conference }}</i>.<br/>
           {% if publication.paper-link %}[<a href="{{ publication.paper-link }}">Paper</a>]{% endif %}
           {% if publication.slide-link %}[<a href="{{ publication.slide-link }}">Slide</a>]{% endif %}
           {% if publication.code-link %}[<a href="{{ publication.code-link }}">Code</a>]{% endif %}
           {% if publication.poster-link %}[<a href="{{ publication.poster-link }}">Poster</a>]{% endif %}
           {% if publication.video-link %}[<a href="{{ publication.video-link }}">Talk</a>]{% endif %}
       </p>
    </li>
    {% endfor %}
</ul>
