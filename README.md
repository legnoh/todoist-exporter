todoist-exporter
====

[![Badge](https://img.shields.io/badge/docker-legnoh/smartmeter--exporter-blue?logo=docker&link=https://hub.docker.com/r/legnoh/smartmeter-exporter)](https://hub.docker.com/r/legnoh/smartmeter-exporter) [![ci](https://github.com/legnoh/todoist-exporter/actions/workflows/ci.yml/badge.svg)](https://github.com/legnoh/todoist-exporter/actions/workflows/ci.yml)

simple prometheus exporter for todoist filter result num

## Usage

- please input filter information to [config.yml](./config.yml)
- please input your environment params to `.env`
  - `TODOIST_API_KEY`
  - `PORT`
- and run it!

```sh
docker run -p $PORT:$PORT --env-file='.env' legnoh/todoist_exporter
```
