<img width="1919" height="1066" alt="Screenshot 2025-07-09 114012" src="https://github.com/user-attachments/assets/28530f9b-e146-4720-9a64-ca9268328f95" />
---

## ⚙️ Technologies Used

- **Frontend:** React.js (Dockerized)
- **Backend:** Node.js + Express (Dockerized)
- **Database:** MongoDB Atlas (Managed)
- **Containerization:** Docker
- **Orchestration:** Kubernetes on AWS EKS
- **Package Management:** Helm
- **Serverless:** AWS Lambda for DB backups
- **Infrastructure as Code:** eksctl & YAML templates

---

## ✅ Steps Implemented

1. **Containerization**
   - Dockerfiles created for `frontend/` and `backend/`.
   - Local Docker build and push commands tested.

2. **EKS Cluster**
   - EKS cluster manually created via AWS Console.
   - `eks-cluster.yaml` provided for reference IaC.

3. **IAM Policies**
   - IAM policies defined in `iam-policies.json` for EKS nodes, ALB controller, Lambda.

4. **Helm Chart**
   - `Chart.yaml`, `values.yaml` and templates for deployment and service created under `helm/`.

5. **Lambda Backup**
   - `backup_db.py` script to take MongoDB Atlas backups and store in S3.

---

## 🚀 How to Use

### 1️⃣ Build & Push Docker Images

```bash
# Backend
cd backend
docker build -t YOUR_DOCKERHUB_USERNAME/backend .
docker push YOUR_DOCKERHUB_USERNAME/backend

# Frontend
cd ../frontend
docker build -t YOUR_DOCKERHUB_USERNAME/frontend .
docker push YOUR_DOCKERHUB_USERNAME/frontend


### Screenshots
# Make sure you have kubectl context set
<img width="1919" height="1066" alt="Screenshot 2025-07-09 114012" src="https://github.com/user-attachments/assets/78119dd0-0410-4121-b0ac-ab88e0ed48c9" />

<img width="1508" height="987" alt="Sc<img width="1914" height="1061" alt="Screenshot 2025-07-09 114054" src="https://github.com/user-attachments/assets/1aa04fd3-a5d5-4b3d-aa0d-dcd7eb26aeef" />
reenshot 2025-07-09 114653" src="https://github.com/user-attachments/assets/43025fd1-be8a-4af8-a1b3-c80563150f07" />
<img width="1672" height="502" alt="S<img width="1919" height="946" alt="Screenshot 2025-07-10 204853" src="https://github.com/user-attachments/assets/2e771eec-3470-4aaa-8382-66f131fbc396" />
creenshot 2025-07-09 122943" src="https://github.com/user-attachments/assets/d432d316-977b-47a5-bf2b-fafb4266864b" />

<img width="1919" height="970" alt="Screenshot 2025-07-10 205036" src="https://github.com/user-attachments/assets/f78a3098-33a2-4f50-90b4-d4d4f6a17598" />
<img width="1917" height="1025" alt="Screenshot 2025-07-10 222223" src="https://github.com/user-attachments/assets/a0b90a17-3ecb-47bc-88da-45cd73a06dbf" />
<img width="1914" height="785" alt<img width="1819" height="937" alt="Screenshot 2025-07-11 200557" src="https://github.com/user-attachments/assets/0b13ae0a-c97c-4d64-9633-7a39c55708ca" />
="<img width="1918" height="931" alt="Screenshot 2025-07-11 192821" src="https://github.com/user-attachments/assets/c0bc2dc9-08a0-459e-bb1c-d3c85acd30ae" />
Screenshot 2025-07-10<img width="1911" height="861" alt="Screenshot 2025-07-11 181539" src="https://github.com/user-attachments/assets/6b5e7c6a-7b8c-4354-9902-8f7febb33b4b" />
 205147" <img width="1918" height="968" alt="Screenshot 2025-07-11 180709" src="https://github.com/user-attachments/assets/604b0d80-9374-4f08-90f9-72e3bbcab536" />
src="<img width="1919" height="899" alt="Screenshot 2025-07-11 020558" src="https://github.com/user-attachments/assets/d8c5a049-62ee-4199-a236-4c9a7754bd87" />
https://github.com/user-attachments/assets/372883aa-f758-415d-b6b3-ebe8ed931240" />
