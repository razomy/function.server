# Welcome to razomy.function

## About

### Organisation

- I want to live(make) in a world of peace, honesty, and support.
- "Razomy" means together; we work together to develop the world.
- Non-profit, investment only.
- Open and without borders; everyone contributing positively is welcome. 

### Product

- Function is a web application for executing operational tasks.

- Functionalities include:
  - Converting files into different types
  - Editing images

- You can extend the functionality as needed:
  - Ensure compliance
  - Make it pluggable for ease of use

## Development

### Get started

1. Install python (3.12) and git
   https://www.python.org/downloads/

2. `mkdir razomy` `cd razomy`
    1. `git clone razomy/python `
    2. `git clone razomy/function.server`
    3. `ln python function.server/razomy/python`

3. Init venv

```shell
python3 -m venv venv
```

4. Install dependencies

```shell
pip inistall -r requirements.txt
```

5. Run

```shell
python main.py
```

### Contribute

1. Make one change per commit
    1. Describe the reason for the change and the solution.
    2. Sign the commit with a proper name and an accessible email for the next 10 years.
2. Make one change type or one solid feature per merge request.

## Deploy

1. setup Google Cloud Platform (GCP)
   https://cloud.google.com

2. setup gcloud
   https://cloud.google.com/sdk/docs/install

3. deploy

```shell
sh deploy.sh
```
