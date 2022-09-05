# jenext

[![GitHub license](https://img.shields.io/github/license/hosein-yousefii/jenext)](https://github.com/hosein-yousefii/jenext/blob/master/LICENSE)
![LinkedIn](https://shields.io/badge/style-hoseinyousefi-black?logo=linkedin&label=LinkedIn&link=https://www.linkedin.com/in/hoseinyousefi)

jenext is a python module to upload files to nextcloud(file server) from local system, it's used with jenkins.

I'm planning to create a jenkins plugin from this python module in order to push artifacts, logs and result to nextcloud which is really helpful.

### NextCloud
Offers an on-premise Universal File Access and sync platform with powerful collaboration capabilities and desktop, mobile and web interfaces.

## What is jenext?
This is difficult to push artifacts, results, logs,... to nextcloud without writing any code from jenkins pipeline so, I wrote a python module to do that for you in a simple way by just set some variables and call a python file.


## Get started
With just 2 steps:

1- set these environments on your system or in your pipeline:
```
# Path to your file which like to upload on Nextcloud
export ARTIFACT_FILE_PATH="/var/jenkins_home/workspace/SAMPLE_PROJECT/target/SIMPLE.jar"

# Destination path on nextcloud (Both "PROJECT_ARTIFACTS" and "SAMPLE" directory should exist on Nextcloud)
export ARTIFACT_NEXTCLOUD_PATH="/PROJECT_ARTIFACTS/SAMPLE"

# Nextcloud url
export NEXTCLOUD_URL="http://NEXTCLOUD_SAMPLE.DOMAIN"

# Nextcloud User
export PUSH_NEXTCLOUD_USER="admin"

# Nextcloud password
export PUSH_NEXTCLOUD_PASS="qazwsx"
```

2- Execute python:
```
python jenext.py
```

## Usage
Just create an isolate environment(optional) and install requirements then Run the code:
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# set variables as explained before.

python jenext.py
```

## Mission:
- Create a Nextcloud plugin for Jenkins.

## How to contribute?
You are able to develop any idea related to it. 
Copyright 2022 Hossein Yousefi yousefi.hosein.o@gmail.com




