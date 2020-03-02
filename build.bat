@echo off
IF NOT EXIST BuildTools (
    mkdir BuildTools
)
cd BuildTools
wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
set /p Input=Enter the version: || set Input=latest
java -jar BuildTools.jar --rev %Input%
MOVE BuildTools/spigot-%Input%.jar ./spigot.jar
pause