from crontab import CronTab

cron = CronTab(user='alexandra')

job = cron.new(command='python bd.py', comment='comment')
job.hour.every(1)

cron.write()
