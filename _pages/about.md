---
layout: main
permalink: /
title: "Overview"
excerpt: "Overview"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a a Gameplay Engineer at [Legacy Labs](https://www.legacylabs.io) and a Ph.D. candidate at the University of Notre Dame advised by [Collin McMillan](https://www3.nd.edu/~cmc/). My research focuses on the application of virtual assistant technology to software engineering tasks, including source code search and source code summarization. In my spare time, I enjoy designing board games and web applications.

<!-- ## Research Interests

Words words words -->


## Education
<div class="education__container" >
  <a class=" education__item" href="https://www.nd.edu/">
    <div class=" education__content">
      <div style="flex:.5">
        <img src="/images/logos/ND.png"/>
      </div>
      <div>
        <p>
         <b class="red"> Ph.D. (Expected 2023)</b><br/>
         <b class="red">M.S. (2021) </b><br/>
          <b>University of Notre Dame</b><br/>
          <i>Computer Science and Engineering</i><br/>
        </p>
      </div>
    </div>
  </a>

  <a class=" education__item" href="https://www.coloradocollege.edu/">
    <div class=" education__content">
      <div style="flex:.5">
        <img src="/images/logos/CC.png"/>
      </div>
      <div>
        <p>
          <b class="red">B.A. (2017)</b><br/>
          <b>Colorado College</b><br/>
          <i>Chemistry and Computer Science</i><br/>
        </p>
      </div>
    </div>
  </a>
</div>

  
<!-- ## Technical Skills

* Primary Languages:
  * Python, Javascript
* Other Languages:
  * Java, C, C++, Ruby
* Machine Learning and NLP Tools:
  * Keras, Tensorflow, Scikit-Learn, Gensim, NLTK, Pandas, BeautifulSoup
* Application Development:
  * Ruby on Rails, React, React Native, Flask, Node.js -->


<!--   <ul>{% for post in site.publications reversed%}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->

## Service
* Program Committee Member for [IEEE/ACM Mining Software Repositories (MSR) Conference](https://conf.researchr.org/home/msr-2022), 2022
* Vice President of the University of Notre Dame Graduate Student Government, 2022
* Social Committee Chair of the University of Notre Dame Graduate Student Government, 2020-2022 

## Publications
{% for post in site.publications reversed  %}
  {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}

  {% if forloop.first %}
  <h3 id="{{this_year}}">{{this_year}}</h3>
  <ul class="publications" style="list-style-type: none; padding-inline-start:0px;">
  {% endif %}
  {% include archive-single-cv.html %}
  {% if forloop.last %}
  </ul>
  {% else %}
  {% if this_year != next_year %}
  </ul>
  <h3 id="{{next_year}}">{{next_year}}</h3>
  <ul style="list-style-type: none; padding-inline-start:0px;">
  {% endif %}
  {% endif %}
{% endfor %}
  
<!-- Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->
  
