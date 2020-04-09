@echo off

echo Checking if BuildTools directory exists
IF NOT EXIST BuildTools (
    echo There is no BuildTools, creating BuildTools directory
    mkdir BuildTools
)

echo Entering BuildTools directory
cd BuildTools

echo Downloading latest BuildTools.jar from spigot server
wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar --no-check-certificate

echo Executing 
java -jar BuildTools.jar --rev latest

echo Moving the result server.jar to main directory
MOVE BuildTools/spigot-%Input%.jar ./spigot.jar

pause