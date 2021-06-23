---
permalink: /
title: "Overview"
excerpt: "Overview"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a 4th year Ph.D. student at the University of Notre Dame advised by [Collin McMillan](https://www3.nd.edu/~cmc/). My research focuses on the application of virtual assistant technology to software engineering tasks. In my spare time, I enjoy playing and [designing](http://mysterywizardgame.com) board games.

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
         <b class="red">Ph.D. (2017-present)</b><br/>
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
          <b class="red">B.A. (2014-2017)</b><br/>
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
  
<!-- ## Service and leadership
* 2017-Present: Events Volunteer
  - Society of Schmitt Fellows, Notre Dame, Notre Dame, IN
* 2015-2016: Volunteer Pharmacy Technician
  - Open Bible Medical Clinic (Formerly TLC Pharmacy), Colorado Springs, CO
 -->