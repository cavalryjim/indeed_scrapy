import scrapy
import csv
import os
import datetime, pytz

class JobSpider(scrapy.Spider):
    name = "ds_jobs"

    start_urls = [
        'https://www.indeed.com/jobs?q=data%20scientist&l=Dallas%2C%20TX&sort=date&fromage=7', #
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
            csv_writer.writerow( [ 'job_id', 'company', 'position' ])
        start = 0
        job_ids = []
        repeating = False

        for job in jobs:
            # print('job')
            job_id = job.css('span[id]').attrib['id'].replace('jobTitle-', '')
            company = job.css('a.companyOverviewLink::text').get()
            position = job.css('span[title]').attrib['title']
            # print(job_id, company, title)
            if job_id not in job_ids:
                csv_writer.writerow( [job_id, company, position] )
                job_ids.append(job_id)
                start += 1
            else:
                repeating = True


        if len(jobs) >= 15 and not repeating:
            url = f"https://www.indeed.com/jobs?q=data%20scientist&l=Dallas%2C%20TX&sort=date&fromage=7&start={start}"
            yield scrapy.Request(
                url = url,
                callback = self.parse
            )
        else:
            print('No page left')


        out_file.close()
