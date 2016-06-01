import shutil
import os

from yum.plugins import TYPE_CORE

requires_api_version = '2.3'
plugin_type = (TYPE_CORE)

delete_dirs = [
  "/usr/lib/locale",
  "/usr/share/locale",
  "/usr/lib/gconv",
  "/usr/lib64/gconv",
  "/usr/bin/localedef",
  "/usr/sbin/build-locale-archive",
  "/usr/share/man",
  "/usr/share/doc",
  "/usr/share/info",
  "/usr/share/gnome/help",
  "/usr/share/backgrounds",
  "/usr/share/wallpapers",
  "/usr/share/centos-logos",
  "/usr/share/cracklib",
  "/var/cache/yum",
  "/sbin/sln",
  "/etc/ld.so.cache",
  "/var/cache/ldconfig",
]

create_dirs = [
  "/var/cache/yum",
  "/var/cache/ldconfig",
]

def close_hook(conduit):
  conduit.info(2, "Running docker image optimizations...")

  for d in delete_dirs:
    shutil.rmtree(d, True)

  for d in create_dirs:
    os.makedirs(d, 0755)
