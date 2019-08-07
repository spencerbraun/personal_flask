title: Creating a personal site from scratch
date: 2019-08-06
published: 2019-08-06
abstract: To create a site that looked and acted the way I wanted, I started from scratch. I'm no expert web dev, so I'll detail what powers this site.
tag: [static, site, flask, python, web, blog, projects]

Between leaving my job and starting grad school, I had a bit of time on my hands and decided it would be a good time to build a personal website. Many developers have them to display their work, but beyond that I figured it would be a good place to leave some thoughts instead of burying them in Evernote. I wasn't sure how big a project this would be, but tried out a bunch of options and ended up quite happy with Github Pages and a flask static site generator.  
  
&nbsp;
  
###### What Else I Considered  
* Jekyll  
Jekyll came up with every Google, and it certainly would have been easier to implement than my solution. However, it runs on Ruby and though I have some experience with it, I was really looking for a Python project. Still, this framework is so appealing I could see moving my site over to it in the future.  

* Pelican  
Pelican is a static site generator written in Python. With a minor amount of setup, I had a site that could display posts and use pre-made themes. However, I had trouble finding a theme that was relatively simple and not too garish, and I had trouble understanding the Pelican build process under the hood. While this would have worked fine, I wanted to understand every piece of the site, so decided to find another route.

* Flask  
I have built several sites in Flask and find it simple and intuitive. Sure they weren't static sites, but I didn't mind paying for some simple hosting. I stumbled across this [post](https://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/) about building a blog in an hour with Flask, and started using that as a base to work off of. Ultimately, I had to ditch almost all of the example code when I decided to go with a static site, plus I was not a fan of the peewee package for SQL management.  
  
&nbsp;
  
###### My Way  
* Github Pages  
After looking around at hosting options, I settled on Github Pages. It is free and relatively straightforward to use - hard to beat that. This meant my site had to be completely static to work with Github (for now at least). Dissatisfied with the static site generators I had already looked into, I wanted a way to use flask and keep the site static.  

* Frozen Flask  / Flask Flatpages  
Luckily, there is a super easy way to turn a flask site into a static site - Frozen Flask. A few extra lines of code is all it takes to take a working Flask app static. I can also choose to remove this bit of code to make it dynamic again if needed.  

* Bootstrap  
Twitter's Bootstrap framework is an easy way to structure the CSS and HTML for a site. I was familiar with it from a project ~4 years ago so turned to it again, though with a steep re-learning curve.  

* Clean Blog Template  
Simple Bootstrap had a number of starting templates to work with. While the site retains very little of the code from the template, it was a good way to refresh my memory of how different tags and styles worked together.


###### How It All Works Together  
What is left is pretty simple - a flask style site that generates static html pages based on certain templates:  
`app.py` - this is the main heart of the site. It generate the routes to each webpage (about, writing, projects, or any blog post). It also freezes the site when `--build` is passed as an arg.  
`settings.py` is called when the app is initiated. It provides some basic setting for how markdown pages are turned into HTML.  
`templates/` holds all of the jinja2 html templates used to render the site. `basestatic.html` is the basic layout of the site, and all other pages inherit the general layout from it.  
`static/` holds everything that doesn't change - images, CSS, JavaScript, etc. While the JavaScript almost entirely came from Bootstrap, I played around a lot with the CSS to get the page to look clean and uncluttered.  
`pages/` holds all of the markdown pages that are turned into blog posts or other content pages. It holds the original markdown that this page was written in. Pages are sorted based on the tags entered at the top.  
`build/` - once changes are good to go, I run `./app.py --build`. This freezes the site contents into the build directory, so all markdown is now html.  
  
&nbsp;
  
That's about it. While I tried a lot of things to get here, I managed to keep the site simple and customizable. Check out the full code [here](https://github.com/spencerbraun/personal_flask) and feel free to contact me with questions.
