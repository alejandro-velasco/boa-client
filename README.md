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
│ *  --name                             TEXT  [default: None] [required]                            │
│ *  --execution                        TEXT  [default: None] [required]                            │
│ *  --organization-id                  TEXT  [default: None] [required]                            │
│ *  --server                           TEXT  [default: None] [required]                            │
│    --submodules    --no-submodules          [default: no-submodules]                              │
│    --branch                           TEXT                                                        │
│    --file                             TEXT  [default: boa.yaml]                                   │
│    --log-level                        TEXT  [default: INFO]                                       │
│    --help                                   Show this message and exit.                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```

| Option                          | Required | Type    | Description                             | Default                 | 
|---------------------------------|----------|---------|-----------------------------------------|-------------------------|
| --url                           | yes      | String  | Git Repository URL to run initial clone | `None`                  |
| --name                          | yes      | String  | name of job                             | `None`                  | 
| --execution                     | yes      | String  | execution number of job                 | `None`                  | 
| --organization-id               | yes      | String  | id of organization that owns the job    | `None`                  | 
| --server                        | yes      | String  | $PROTOCOL://HOSTNAME of boa-manager     | `None`                  | 
| --submodules / --no-submodules  | no       | Boolean | Pull in or ignore git submodules        | `--no-submodules`       |
| --branch                        | no       | String  | Branch to clone                         | `None (default branch)` |
| --file                          | no       | String  | file containing boa job specs           | `boa.yaml`              |
| --log-level                     | no       | String  | log level                               | `INFO`                  |
| --help                          | no       | String  | displays help options                   | `None`                  |