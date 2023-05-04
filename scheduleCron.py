from crontab import CronTab

cron = CronTab(user='alexandra')

job = cron.new(command='python example1.py', comment='comment')
job.hour.every(1)

cron.write()