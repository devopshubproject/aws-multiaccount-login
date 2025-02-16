# aws-login-portal
This repo contains flask application code which will facilitate us logging into our multiple aws accounts from a single portal


### How to Run

```sh
docker build -t aws-login-app .
```

```sh
docker run -d -p 8080:5000 \   
  -e AWS_ACCESS_KEY_ID="env.AWS_ACCESS_KEY_ID" \
  -e AWS_SECRET_ACCESS_KEY="env.AWS_SECRET_ACCESS_KEY" \
  -e AWS_DEFAULT_REGION="env.AWS_DEFAULT_REGION" \
  aws-login-app

