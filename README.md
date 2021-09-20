todoist-exporter
====

[![ci](https://github.com/legnoh/todoist_exporter/actions/workflows/ci.yml/badge.svg)](https://github.com/legnoh/todoist_exporter/actions/workflows/ci.yml)

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
