## E.Multipass.1: MACOs  Installation Steps

Multipass by default does not support Windows 10 Home. You will need to install Virtual Box for using Multipass on Windows 10 Home.

* Download Install latest version of Multipass <https://multipass.run/docs/installing-on-macos.run/>
* To Launch an instance (by default you get the current Ubuntu LTS) : multipass launch --name ubuntu-lts

## E.Multipass:  Example:1 To install multipass

```
psenthil$  brew cask install multipass
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/core).
==> New Formulae
```

## E.Multipass:  Example:2 To Check vesion
```
psenthil$ multipass version                              
multipass  1.0.0+mac
multipassd 1.0.0+mac
```

## E.Multipass:  Example:2 To Launch ubuntu-lts

```
multipass launch --name ubuntu-lts
One quick question before we launch … Would you like to help                    
the Multipass developers, by sending anonymous usage data?
This includes your operating system, which images you use,
the number of instances, their properties and how long you use them.
We’d also like to measure Multipass’s speed.

Send usage data (yes/no/Later)? ys
Please answer yes/no/Later: ys
Please answer yes/no/Later: yes
Thank you!

```

## E.Multipass:  Example:3 To Find available images

```
psenthil$ multipass find
Image                   Aliases           Version          Description
snapcraft:core          core16            20200221         Snapcraft builder for Core 16
snapcraft:core18                          20200221         Snapcraft builder for Core 18
16.04                   xenial            20200218.1       Ubuntu 16.04 LTS
18.04                   bionic,lts        20200218         Ubuntu 18.04 LTS
```
