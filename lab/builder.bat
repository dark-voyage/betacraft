::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFDxRQgGPPX+1FIk47fvw++WXnn0PW+g6e5vI5raLNOEQ+ETiYaosxWlfjNgwDh5MfxG5bwkg52dBuQQ=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+IeA==
::cxY6rQJ7JhzQF1fEqQJhZksaHWQ=
::ZQ05rAF9IBncCkqN+0xwdVsFAlTMbQs=
::ZQ05rAF9IAHYFVzEqQISDS91DCa3FUeeI4d8
::eg0/rx1wNQPfEVWB+kM9LVsJDCaXNWe+A6d8
::fBEirQZwNQPfEVWB+kM9LVsJDCaXNWe+A6d8
::cRolqwZ3JBvQF1fEqQIEIB4UXwGQKm6oRrYT5fjy4++V4k4PUeMrfYub2K3OB+Ud70jlYZk/tg==
::dhA7uBVwLU+EWHu31mNQ
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATE1nESCVtWVUSlOWW/C7QI5/qb
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFDxRQgGPPX+1FIk47fvw++WXnn0PW+g6e5vI5raLNOEQ+ETiYaoP025b2OkZBRdcMBeza28=
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off

title BETA BUILDER BY GENEMATOR

echo Checking if builds directory exists
if not exist builds (
    echo There is no Builds, creating BuildTools directory
    mkdir builds
)

echo Entering Builds directory
cd builds

echo Downloading latest BuildTools.jar from spigot server
curl --insecure -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar 

set /p Input=Enter the version of Minecraft: || set Input=1.15.2
rem You can make it latest

echo Executing 
java -jar BuildTools.jar --rev %Input%

echo Moving the result server.jar to main directory
ren "spigot-%Input%.jar" "server.jar"
move "server.jar" ..

pause

