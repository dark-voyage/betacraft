#!/usr/bin/env bash
pyinstaller -y -F -i "/Users/mumtoza/Documents/GitHub/betacraft/assets/repo/betacraft.ico" --add-data "/Users/mumtoza/Documents/GitHub/betacraft/assets":"assets/" -n Beta Builder  "/Users/mumtoza/Documents/GitHub/betacraft/builder.py"
exit