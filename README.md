# Boa Client: Clientside CLI for Boa CI Jobs

## Overview

This project is a minimally viable agent software designed to be installable via python pip. Once installed a user can run the `boa` CLI to clone a git project, and run simple CI jobs.

## Prerequisites

`boa` requires the following to function:
- Python 3.11 or later
- Git

## Installation

To install, the package must first be built, then installed via pip.

### Build

Install Python package build tools
```bash
python3 -m pip install --upgrade build
```

Build the Pip Package. The final package will be located under the dist folder
```bash
python3 -m build
```

### Install

To install the locally build pip package, run a pip install on the `whl` file.
```
# set VERSION to the appropriate versioned release
VERSION="0.0.1"
python3 -m pip install --upgrade dist/boa_client-$VERSION-py3-none-any.whl
```

## Usage

 Usage: boa [OPTIONS]

```bash
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --url                              TEXT  [default: None] [required]                            │
│    --submodules    --no-submodules          [default: no-submodules]                              │
│    --branch                           TEXT                                                        │
│    --name                             TEXT  [default: workspace]                                  │
│    --file                             TEXT  [default: boa.yaml]                                   │
│    --log-level                        TEXT  [default: INFO]                                       │
│    --help                                   Show this message and exit.                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```

| Option                          | Required | Type    | Description                             | Default                 | 
|---------------------------------|----------|---------|-----------------------------------------|-------------------------|
| --url                           | yes      | String  | Git Repository URL to run initial clone | `None`                  |
| --submodules / --no-submodules  | no       | Boolean | Pull in or ignore git submodules        | `--no-submodules`       |
| --branch                        | no       | String  | Branch to clone                         | `None (default branch)` |
| --name                          | no       | String  | name of workspace folder                | `workspace`             |
| --file                          | no       | String  | file containing boa job specs           | `boa.yaml`              |
| --log-level                     | no       | String  | log level                               | `INFO`                  |
| --help                          | no       | String  | displays help options                   | `None`                  |