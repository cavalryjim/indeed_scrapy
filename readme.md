# Indeed Scrapy Project

This code was created for a tutorial that scrapes job information from the website Indeed.

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
(indeed_scrapy) $ pipenv install
```

Run the scrapy crawler.

```
(indeed_scrapy) $ scrapy crawl ds_jobs
```

When you are finished, stop the virtual environment.

```
(indeed_scrapy) $ exit
$
```
