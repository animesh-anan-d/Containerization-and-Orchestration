# EKS MERN App Deployment

## What’s Included
- `eks-cluster.yaml` — EKS cluster config
- `lambda/backup_db.py` — Lambda to backup DB
- `helm/` — Helm chart for MERN app

## Steps
1. Create EKS: `eksctl create cluster -f infra/eks-cluster.yaml`
2. Deploy Nodegroup (auto in config)
3. Deploy Helm: `helm install mern-app helm/`
4. Lambda deploy via console or Terraform

## Notes
- CloudWatch logs integrated by EKS
- Lambda writes backups to S3
