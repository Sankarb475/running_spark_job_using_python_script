echo -e "Starting the Application Processing Engine Launcher!!"
nohup python ${APP_HOME}/conf/SparkLauncher.py > /dev/null 2>&1 &
echo $! > SparkLauncher_run.pid
