<p align="center">
  <a href="https://t.me/bsba_group">
    <img src="assets/betacraft.png" width="200" height="200">
  </a>
  <h1 align="center">BetaCraft</h1>
</p>

**This server was built with [Spigot](https://www.spigotmc.org/) in [Java](https://www.java.com/en/). This server works as plugin modular, so don't worry about adding your own plugins. It will not affect to the server's working process. Just, don't forget to restart server and you're ready to go!
If you want to create your own server with my codes, just head to the [Deploy your own](#deploy-your-own) section.**
 
## Deploy Your Own
**To deploy your own server with my instances follow the steps provided below:**

1. Download my source codes from [there](#download-sources).
2. Unzip my master source code.
3. Save the folder somewhere you can remember
4. Enter the folder
5. Run `build.bat` file
6. Wait until it finishes
7. Run `start.bat` file after build completion
8. Open minecraft
9. Add new server with `localhost:25565` credential
10. Voila! You're ready to go!

## Sharing server between localhost or public

#### If you live in country where every citizen have public ip adress do the following:

For localhost:
1. Open CMD or Powershell
2. Type ipconfig
3. Find your IPv4 adress connecting you to your router
4. Share your adress in this form: <ip>:25565
`Example: 192.168.1.2:25565 or 10.10.0.2:25565`

For public:
1. Open browser
2. Type `what's my ip`
3. Copy adress
4. Enter router
5. Port forward internal 25565 to outer 25565
4. Share the result like this: <ip>:25565

#### If you live in a country where the whole country uses a single ip adress like me do the following:

For localhost do the same as I mention below in public one, but for public you need to do something more extra:
1. Download ngrok from [download sources](#download-sources)
2. <a href="https://ngrok.com/">Open ngrok homepage</a>
3. Register and follow guides from ngrok
4. When you finish setting up your ngrok instance execute this:
```powershell
./ngrok tcp 25565
```
5. Copy ip adress and share it.

## Download Sources
<a href="https://github.com/sakhib-orzklv/automator/archive/master.zip">Download Latest Update</a>
<a href="https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip">Download ngrok package</a>

## Documentations
* **Spigot** - [Wiki](https://www.spigotmc.org/wiki/spigot/)
* **Ngrok** - [Website](https://ngrok.com/docs)

> The server page is still in beta phase so feel free to [open issues](https://github.com/sakhib-orzklv/betacraft/issues/new) and give me some suggestions.
---

> **Important Note:** Under the MIT license, if you're running your own instance, you should add a link to the source [(this repository)](https://github.com/sakhib-orzklv/betacraft) in your bot's bio or about page. If you're modifying this source and making your own bot, you should link to the source of your own version of the bot according to the MIT license. Check [LICENSE](LICENSE) for more info.

<p align="center">
    <a href="https://bsba.gq"><b>BetaCraft</b></a> icon is from <a href="https://t.me/sakhib_orzklv/">Genemator Sakhib</a> by Sokhibjon Orzikulov. Copyright to <a href="https://bsba.gq"><b>BSBA TEAM</b></a>
</p>
