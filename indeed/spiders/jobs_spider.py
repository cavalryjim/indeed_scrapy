import scrapy
import csv
import os
import datetime, pytz

class JobSpider(scrapy.Spider):
    name = "ds_jobs"
    job_ids = []
    start = 0

    start_urls = [
        # This url will return an html file with data scientist jobs in Dallas TX.
        # The job postings will be sorted by date from the past 7 days.
        'https://www.indeed.com/jobs?q=data%20scientist&l=Dallas%2C%20TX&sort=date&fromage=7',
        # 'https://www.indeed.com/jobs?q=data%20scientist&l=Houston%2C%20TX&sort=date&fromage=7',
    ]

    def parse(self, response):
        now = pytz.timezone("America/Chicago").localize(datetime.datetime.now())
        file_name = 'jobs_' + now.strftime("%Y-%m-%d")  + '.csv'
        jobs = response.css("div.result")

        if os.path.exists(file_name):
            out_file = open(file_name, 'a')
            csv_writer = csv.writer(out_file)
        else:
            out_file = open(file_name, 'w')
            csv_writer = csv.writer(out_file)
            csv_writer.writerow( [ 'job_id', 'city', 'company', 'position' ])

        repeating = False

        for job in jobs:
            # print('job')
            job_id = job.css('span[id]').attrib['id'].replace('jobTitle-', '')
            company = job.css('a.companyOverviewLink::text').get()
            position = job.css('span[title]').attrib['title']
            #<div class="companyLocation">
            city = job.css('div.companyLocation::text').get()
            # print(job_id, company, title)
            if job_id not in JobSpider.job_ids:
                csv_writer.writerow( [job_id, city, company, position] )
                self.job_ids.append(job_id)
                self.start += 1
            else:
                repeating = True

        if len(jobs) >= 15 and not repeating:
            url = response.url.split('&start=')[0] + "&start=" + str(self.start)
            print(url)
            yield scrapy.Request(
                url = url,
                callback = self.parse
            )
        else:
            print('No page left')
            # self.start = 0


        out_file.close()
