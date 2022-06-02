# Indeed Scrapy Project

This is a tutorial for scraping job information from the job posting website Indeed.

I recommend using __pipenv__ for these projects.  If you don't already have it installed,
use this command:

```
$ pip install pipenv
```

Navigate to the directory / folder where you want to create this project.  I keep
my projects in a 'Projects' folder.

```
$ cd Projects
$ mkdir indeed_scrapy
$ cd indeed_scrapy
```

Start a new virtual environment using pipenv.

```
$ pipenv shell
```

Install the required python packages.

```
$ pipenv install
```

Run the scrapy crawler.

```
$ scrapy crawl ds_jobs
```
