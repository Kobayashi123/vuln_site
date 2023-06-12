# vuln_site

## Description

This is a web application to verify various vulnerabilities.
In fact, it can be run using Docker.

## Requirement

docker 20.10.17

## Usage

### 1. Clone this repository

```bash
git clone git@github.com:Kobayashi123/vuln_site.git
```

or

```bash
git clone https://github.com/Kobayashi123/vuln_site.git
```

### 2. Change the working directory

```bash
cd vuln_site
```

### 4. Run the container

Please enter the directory of the vulnerability you wish to study.

```bash
cd SSRF
```

All that remains is to use docker-compose to start it up.

```bash
docker-compose up -d
```

## Licence

[Apache License, Version2.0](https://github.com/Kobayashi123/vuln_site/blob/main/LICENSE)

## Author

[Kobayashi123](https://github.com/Kobayashi123)
