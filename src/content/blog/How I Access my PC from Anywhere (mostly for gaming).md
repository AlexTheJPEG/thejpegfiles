---
title: How I Access my PC from Anywhere (mostly for gaming)
slug: how-i-access-my-pc-from-anywhere-mostly-for-gaming
tags: ["tech", "gaming", "pc", "laptop", "homelab"]
dateCreated: 2024-04-07
dateUpdated: 2024-10-26
excerpt: (ARCHIVED FROM OLD WEBSITE) An overview of how I made my own remote gaming setup, with updates
---
I use my PC to play games and do other heavy-workload stuff. However, I don't have access to it all the time. I couldn't bring my PC to my college dorm, and my laptop just didn't cut it for certain games like _Like a Dragon: Infinite Wealth_, which at the time was slated to release after my winter break. To play these graphically-intensive games, I used to rent a cloud PC from [Shadow](https://shadow.tech), which admittedly is a pretty convenient service, but the monthly subscription price was pretty hefty. So during the break, I devised a method that would let me remotely connect to my PC and use it as if I was still at home. I'll write a rough summary of what I did to accomplish this here, both for me to be able to replicate the setup if I ever lose it, and for anyone reading this who is in the same situation as I am.

For starters, I use [Parsec](https://parsec.app) to connect to my PC. As long as my PC's on, I can just connect to it and start using it. The problem is, that would require keeping my PC on 24/7, and I did not want to waste so much electricity; thus, I had to find a way to also turn my computer on and off. But how can I do that without pressing the power button?

At first, I thought this would be impossible, then I found something called ["Wake-on-LAN"](https://en.wikipedia.org/wiki/Wake-on-LAN). From my understanding, using another device, I can send a "magic packet" to my PC through Ethernet that signals to turn it on. I have no idea how this actually works, but it was perfect for my use case. I just so happened to be running my Lenovo Thinkcentre (which runs some self-hosted services and Discord bots) on the same network as my PC. I also had to enable Wake-on-LAN functionality both through my PC's BIOS and Windows network settings. This is well-documented online; I just followed [this guide](https://www.windowscentral.com/how-enable-and-use-wake-lan-wol-windows-10). Keep in mind though that BIOS updates can reset all your settings, including the one to enable Wake-on-LAN. I learned that the hard way.

With all of these pieces into place, I created a step-by-step plan for remotely accessing my PC:

1. SSH into my Thinkcentre (all of my devices are in a [Tailscale](https://tailscale.com) mesh VPN, so I can connect any one of my devices to one another via their 100.x.y.z IP).
2. Use the [`wakeonlan`](https://manpages.debian.org/bookworm/wakeonlan/wakeonlan.1.en.html) command along with the MAC address of my PC.
3. Just wait a minute or two for my PC to boot up and for the Parsec service to initialize. Turns out that Parsec allows running the service on boot, so I can also log into my computer remotely.
4. When I'm done using it, I simply shut down my PC through the start menu, but not before closing any running apps, notably Steam, since it hanged the shutdown once.

What happens, though, if I for some reason can't SSH into my Thinkcentre (such as when I accidentally forgot to back up my SSH keys when I switched from Windows to Linux on my main laptop)? I found a web app called [UpSnap](https://github.com/seriousm4x/UpSnap) which allows me to send the Wake-on-LAN packet to my PC through my browser. I just have to spin up a Docker container for it, publish it to an unused port, and log into it through my Thinkcentre's Tailscale IP. Finally, in the settings, I added my PC by supplying its MAC address and 192.168.x.y IP. Turning on my PC is now as simple as pressing a button. I'm still debating on whether I should keep this
method or go back to SSH when I can go back home and fix it.

> [!NOTE] Oct 26 Update
> Since Tailscale now offers SSH across devices on your tailnet to general consumers, I set that up instead of fiddling with SSH keys so I can run terminal commands on my server whenever I want.

From my experience, the Parsec client works like a charm on Windows. However, using Parsec on a Linux client to a Windows host isn't stellar, but it gets the job done. I can play pretty much all the games I have comfortably. The graphics can be blurry and pixelated at times, but that's to be expected when streaming an entire desktop over an Internet connection. One thing I wish worked better is mic passthrough, which lets me play games like Lethal Company and Helldivers 2 with in-game voice chat. This is entirely possible between Windows clients and hosts thanks to the experimental mic passthrough feature, but the Linux client unfortunately does not have that yet. Someone online suggested an app called [AudioRelay](https://audiorelay.net), which was relatively straightforward to set up, so now I can take the mic connected to my laptop and send it over as mic input to my PC. It's a more cumbersome method than simply using in-app mic passthrough, but it seems to work.

Now, with this setup, there is the obvious drawback of having my PC on at home unattended. But the only people at home are my parents, and I trust them enough to not snoop around. There are no monitors or peripherals connected to my PC; it's just the ethernet cable and power supply cable. I can pass keyboard and mouse inputs from my laptop (obviously) and Parsec has a virtual display driver that can simulate a 1080p monitor for me.

With this, I'm able to play all of my games as if I brought my PC with me to my dorm, and I don't have to install a lot of the intensive games on my laptop either, which saves a lot of disk space. Granted, I can't play any games that require super precise inputs with minimal lag or latency, so rhythm games are out of the question, but I can play the rest of my catalog without any major issues. And for someone who doesn't care about super top-of-the-line response times
or graphical fidelity (yet), that's all I really need.