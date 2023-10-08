## configure aws cli
1. run
```
aws configure sso
```
2. run
```
aws ec2 describe-vpcs –-profile admin-1
```
3. run
```
aws s3 ls --profile admin-1
```
4. login
```
aws sso login --profile admin-1
```

## Access the CDK
1. get userid and accountid
```
aws sts get-caller-identity --profile admin-1
```
2. get current zone
```
aws configure get region --profile admin-1
```
3. to bootstrap 
```
cdk bootstrap aws://ac#/region --profile admin-1
```