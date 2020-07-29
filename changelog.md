# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.2] - 2020-07-28
### Added
- Support overriding the datasources. PR#10
- add new data source - Fedora release names - PR#11
- added an introduction to the readme. - PR#12


## [0.0.1] - 2020-07-27
### Added
- added `Dockerfile` to allow the application to be built
  and run inside a container. PR#7
- add a simple flask wrapper to allow the API to be called over http. PR#6
- run the code through `black` and `flake8` and fix the violations PR#5
  this is not set to auto happen yet.
- Add github action to detect issues in the data set PR#4
- Initial version of the module and a small CLI application to use it. PR#1
