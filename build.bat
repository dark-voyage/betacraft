@echo off
IF NOT EXIST BuildTools (
    mkdir BuildTools
)
cd BuildTools
wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
java -jar BuildTools.jar --rev latest
MOVE BuildTools/spigot-%Input%.jar ./spigot.jar
pause