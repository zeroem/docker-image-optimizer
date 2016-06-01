## Docker Image Optimizer

A yum plugin to perform the cleanup steps found in [contrib/mkimage-yum.sh](https://github.com/docker/docker/blob/master/contrib/mkimage-yum.sh) every time yum runs.

### Installation
  - Copy `docker-image-optimizer.py` into the yum plugins directory, `/usr/lib/yum-plugins`
  - Copy `docker-image-optimizer.conf` into the yum plugins config directory, `/etc/yum/pluginconf.d/`
  - Ensure plugins are enabled in your yum.conf

  ```ini
    [main]
    plugins=1
  ```

### Testing

```
docker build .
```

It _shouldn't_ blow up...
