#35 17 * * * cd /home/ubuntu/OpenTushare/ && sh z_crontab.sh 1> log.crontab.stdout 2> log.crontab.stderr
cd /home/ubuntu/OpenTushare && python x_analyse.py append
