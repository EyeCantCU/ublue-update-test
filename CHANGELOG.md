# Changelog

## 1.0.0 (2023-07-06)


### Features

* add log for when update is complete ([f3992f3](https://github.com/EyeCantCU/ublue-update-test/commit/f3992f39c5fae0db82e43e4192af67c7e9a7efce))
* add proof-of-concept containerfile for this project ([aeeb3c0](https://github.com/EyeCantCU/ublue-update-test/commit/aeeb3c08e459488b7dbd4a9737a3fa25f7f3a92a))
* add RPM build and restructure to make it work ([9642188](https://github.com/EyeCantCU/ublue-update-test/commit/9642188e94a1d0c147b9b78efa37fba324eb23a3))
* added --check option to run through update checks and exit ([ac0523b](https://github.com/EyeCantCU/ublue-update-test/commit/ac0523bea189c3216bdb45962d847a41169cdca1))
* Implement system update check module and notification ([50b02dd](https://github.com/EyeCantCU/ublue-update-test/commit/50b02dd5fe4470ef0a889c10c23aec692c5ea5d7))
* made config loading more robust ([722c956](https://github.com/EyeCantCU/ublue-update-test/commit/722c956392235d268eacee803d1ccd00f930ab85))
* moved config format to toml, cleaned up config logic to default to /usr/etc ([2c47f12](https://github.com/EyeCantCU/ublue-update-test/commit/2c47f12d942b9b2c79c277369c9f015af67fd15d))
* Update public cosign key ([71ab9f6](https://github.com/EyeCantCU/ublue-update-test/commit/71ab9f696425935455b7d873fb5e431040b6a187))


### Bug Fixes

* Adjust update service and timer ([2dc0ccc](https://github.com/EyeCantCU/ublue-update-test/commit/2dc0ccc80cdaa850c7acd2729e883118e2212ad5))
* apply some small python cleanups ([69e42d0](https://github.com/EyeCantCU/ublue-update-test/commit/69e42d0c74a2d5f0a78881ca1fd9494bad39c919))
* **config:** fix breakage when using fallback config, improved config logic to be more flexible ([f167dc9](https://github.com/EyeCantCU/ublue-update-test/commit/f167dc970d7b38e4ecf6d85895e800ce16760063))
* formatting errors after merge ([d3f011a](https://github.com/EyeCantCU/ublue-update-test/commit/d3f011ae4f46dce352ed46e61d20029845bd1fde))
* Make update scripts executable in spec file ([d57ea4e](https://github.com/EyeCantCU/ublue-update-test/commit/d57ea4ebbf080173d3cb9a56dbf89cd6bb1e11f5))
* moved log.info outside of if check ([ed25b1c](https://github.com/EyeCantCU/ublue-update-test/commit/ed25b1c3e17bcd8a64b2b60f26c73ba8a20bb404))
* remove 'sudo' from 'sudo install' in rpm spec ([8d80161](https://github.com/EyeCantCU/ublue-update-test/commit/8d801611a863338552a10047aa64cfb86be35b5f))
* remove unused makefile recipes ([93ea24a](https://github.com/EyeCantCU/ublue-update-test/commit/93ea24a290aaae4e66bec1397655c67ffcf4cf12))
* removed exit() and print() function used for debugging ([2eca189](https://github.com/EyeCantCU/ublue-update-test/commit/2eca1892a262ff7b1381dfcecb65d27fa5cd203e))
* single line that makes the app not executable ([08706a5](https://github.com/EyeCantCU/ublue-update-test/commit/08706a546b8199bcad6ee1a611185e1ed1a82729))
* **systemd timer:** fixed spelling of persistent ([0c74fa2](https://github.com/EyeCantCU/ublue-update-test/commit/0c74fa24f8e7eab557fa7030571b671bee964b62))
* update comment ([3a6aff7](https://github.com/EyeCantCU/ublue-update-test/commit/3a6aff771def651f25fcbec6ff5504ae49666669))
* update install instructions to new image location ([eba75de](https://github.com/EyeCantCU/ublue-update-test/commit/eba75de2e56d96afd4b409427339206f242cb28e))
* use tabs not spaces ([7e33290](https://github.com/EyeCantCU/ublue-update-test/commit/7e332909d7a9443a0ba895515ac71b6fa7d3a56b))
* use the correct name ([2848f64](https://github.com/EyeCantCU/ublue-update-test/commit/2848f6434eaca1c71680e24250d03bf23a0c1504))

## 1.0.0 (2023-07-04)


### Features

* add log for when update is complete ([f3992f3](https://github.com/ublue-os/ublue-update/commit/f3992f39c5fae0db82e43e4192af67c7e9a7efce))
* add proof-of-concept containerfile for this project ([aeeb3c0](https://github.com/ublue-os/ublue-update/commit/aeeb3c08e459488b7dbd4a9737a3fa25f7f3a92a))
* add RPM build and restructure to make it work ([9642188](https://github.com/ublue-os/ublue-update/commit/9642188e94a1d0c147b9b78efa37fba324eb23a3))
* added --check option to run through update checks and exit ([ac0523b](https://github.com/ublue-os/ublue-update/commit/ac0523bea189c3216bdb45962d847a41169cdca1))
* made config loading more robust ([722c956](https://github.com/ublue-os/ublue-update/commit/722c956392235d268eacee803d1ccd00f930ab85))
* moved config format to toml, cleaned up config logic to default to /usr/etc ([2c47f12](https://github.com/ublue-os/ublue-update/commit/2c47f12d942b9b2c79c277369c9f015af67fd15d))


### Bug Fixes

* Adjust update service and timer ([2dc0ccc](https://github.com/ublue-os/ublue-update/commit/2dc0ccc80cdaa850c7acd2729e883118e2212ad5))
* apply some small python cleanups ([69e42d0](https://github.com/ublue-os/ublue-update/commit/69e42d0c74a2d5f0a78881ca1fd9494bad39c919))
* formatting errors after merge ([d3f011a](https://github.com/ublue-os/ublue-update/commit/d3f011ae4f46dce352ed46e61d20029845bd1fde))
* Make update scripts executable in spec file ([d57ea4e](https://github.com/ublue-os/ublue-update/commit/d57ea4ebbf080173d3cb9a56dbf89cd6bb1e11f5))
* moved log.info outside of if check ([ed25b1c](https://github.com/ublue-os/ublue-update/commit/ed25b1c3e17bcd8a64b2b60f26c73ba8a20bb404))
* remove 'sudo' from 'sudo install' in rpm spec ([8d80161](https://github.com/ublue-os/ublue-update/commit/8d801611a863338552a10047aa64cfb86be35b5f))
* remove unused makefile recipes ([93ea24a](https://github.com/ublue-os/ublue-update/commit/93ea24a290aaae4e66bec1397655c67ffcf4cf12))
* single line that makes the app not executable ([08706a5](https://github.com/ublue-os/ublue-update/commit/08706a546b8199bcad6ee1a611185e1ed1a82729))
* **systemd timer:** fixed spelling of persistent ([0c74fa2](https://github.com/ublue-os/ublue-update/commit/0c74fa24f8e7eab557fa7030571b671bee964b62))
* update comment ([3a6aff7](https://github.com/ublue-os/ublue-update/commit/3a6aff771def651f25fcbec6ff5504ae49666669))
* update install instructions to new image location ([eba75de](https://github.com/ublue-os/ublue-update/commit/eba75de2e56d96afd4b409427339206f242cb28e))
* use tabs not spaces ([7e33290](https://github.com/ublue-os/ublue-update/commit/7e332909d7a9443a0ba895515ac71b6fa7d3a56b))
* use the correct name ([2848f64](https://github.com/ublue-os/ublue-update/commit/2848f6434eaca1c71680e24250d03bf23a0c1504))

## 1.0.0 (2023-07-03)


### Features

* add log for when update is complete ([f3992f3](https://github.com/akdev1l/ublue-update/commit/f3992f39c5fae0db82e43e4192af67c7e9a7efce))
* add proof-of-concept containerfile for this project ([aeeb3c0](https://github.com/akdev1l/ublue-update/commit/aeeb3c08e459488b7dbd4a9737a3fa25f7f3a92a))
* add RPM build and restructure to make it work ([9642188](https://github.com/akdev1l/ublue-update/commit/9642188e94a1d0c147b9b78efa37fba324eb23a3))
* added --check option to run through update checks and exit ([ac0523b](https://github.com/akdev1l/ublue-update/commit/ac0523bea189c3216bdb45962d847a41169cdca1))
* made config loading more robust ([722c956](https://github.com/akdev1l/ublue-update/commit/722c956392235d268eacee803d1ccd00f930ab85))


### Bug Fixes

* apply some small python cleanups ([69e42d0](https://github.com/akdev1l/ublue-update/commit/69e42d0c74a2d5f0a78881ca1fd9494bad39c919))
* formatting errors after merge ([d3f011a](https://github.com/akdev1l/ublue-update/commit/d3f011ae4f46dce352ed46e61d20029845bd1fde))
* Make update scripts executable in spec file ([d57ea4e](https://github.com/akdev1l/ublue-update/commit/d57ea4ebbf080173d3cb9a56dbf89cd6bb1e11f5))
* moved log.info outside of if check ([ed25b1c](https://github.com/akdev1l/ublue-update/commit/ed25b1c3e17bcd8a64b2b60f26c73ba8a20bb404))
* remove 'sudo' from 'sudo install' in rpm spec ([8d80161](https://github.com/akdev1l/ublue-update/commit/8d801611a863338552a10047aa64cfb86be35b5f))
* remove unused makefile recipes ([93ea24a](https://github.com/akdev1l/ublue-update/commit/93ea24a290aaae4e66bec1397655c67ffcf4cf12))
* single line that makes the app not executable ([08706a5](https://github.com/akdev1l/ublue-update/commit/08706a546b8199bcad6ee1a611185e1ed1a82729))
* update comment ([3a6aff7](https://github.com/akdev1l/ublue-update/commit/3a6aff771def651f25fcbec6ff5504ae49666669))
* update install instructions to new image location ([eba75de](https://github.com/akdev1l/ublue-update/commit/eba75de2e56d96afd4b409427339206f242cb28e))
* use tabs not spaces ([7e33290](https://github.com/akdev1l/ublue-update/commit/7e332909d7a9443a0ba895515ac71b6fa7d3a56b))
* use the correct name ([2848f64](https://github.com/akdev1l/ublue-update/commit/2848f6434eaca1c71680e24250d03bf23a0c1504))
