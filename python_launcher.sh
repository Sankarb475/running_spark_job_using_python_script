echo -e "Starting the Hermes Processing Engine Launcher!!"
nohup python ${APP_HOME}/conf/SparkLauncher.py > /dev/null 2>&1 &
echo $! > SparkLauncher_run.pid
