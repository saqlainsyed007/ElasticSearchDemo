# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.box_check_update = true

  config.vm.network "forwarded_port", guest: 8000, host: 7000

  config.vm.synced_folder ".", "/home/vagrant/source/"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
    vb.cpus = 2
  end

  $SERVER_SETUP = <<-SCRIPT
    export DEBIAN_FRONTEND=noninteractive
    apt-get update
    apt-get install -y git
    apt-get install -y build-essential
    apt-get install -y libreadline6-dev
    apt-get install -y libyaml-dev
    apt-get install -y libsqlite3-dev
    apt-get install -y sqlite3
    apt-get install -y autoconf
    apt-get install -y libgdbm-dev
    apt-get install -y libncurses5-dev
    apt-get install -y automake
    apt-get install -y libtool
    apt-get install -y bison
    apt-get install -y libffi-dev
    apt-get install -y postgresql-client
    apt-get install -y postgresql-contrib
    apt-get install -y virtualenvwrapper
    apt-get build-dep -y psycopg2
    apt-get build-dep -y pillow
  SCRIPT

  config.vm.provision "shell", inline: $SERVER_SETUP, privileged: true
end
