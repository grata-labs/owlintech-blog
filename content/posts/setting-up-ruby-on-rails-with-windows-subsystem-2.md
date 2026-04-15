---
title: "Setting up Ruby on Rails with Windows Subsystem for Linux 2"
date: 2020-06-21T16:21:07+00:00
draft: false
summary: "Step-by-step guide on getting Ruby on Rails running on a WSL2 Ubuntu Distro."
cover:
  image: "/content/images/2020/06/GOQb6uBi_400x400.jpg"
  alt: "Setting up Ruby on Rails with Windows Subsystem for Linux 2"
  relative: false
---
<!--more-->
I wanted to use Ruby on Rails with good tooling on my Windows computer, which made WSL2 the obvious choice. I thought I'd just fire up an Ubuntu VM and off I go. I came across some issues though. There are many tools missing when you just start up.

Here I'll step you through how to get RoR working in WSL2. This guide presumes you already have [WSL2](<https://docs.microsoft.com/en-us/windows/wsl/install-win10>) set up on your computer. I'll be starting with a fresh Ubuntu distro.
    
    
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
    sudo apt-get update
    sudo apt-get install git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev nodejs yarn

First get the distribution lists for nodejs and yarn, update the lists, and install them. Also included are a few other libraries you'll need. This is where the magic is, you couldn't possibly know you need all this stuff.
    
    
    git clone https://github.com/rbenv/rbenv.git ~/.rbenv
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc

Clone the rbenv repo and add the tooling to your `.bashrc` file
    
    
    git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
    echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
    exec $SHELL

Clone the ruby-build repo as a plugin to rbenv. Add its tooling to your `.bashrc` file. Then reload the shell.
    
    
    rbenv install 2.7.1
    rbenv global 2.7.1
    ruby -v
    
    gem install rails
    rails -v

Finally you'll be able to install ruby and the rails gem. 

I've [created a gist](<https://gist.github.com/owlstronaut/2afaad823c6883b9c7a5e427034e1d72>) if you just want to run the script and get up-and-running.

![](/content/images/2020/06/image.png)All Ready to start Railing away!

And what's the coolest part of this? You can type `code .` in the folder you want to develop, and VSCode will fire up on your Windows computer and automatically connect to the Windows subsystem! How cool is that?
