# Secrets Manager Secure Retrieval (Python)

This project demonstrates secure secret retrieval using Python and AWS Secrets Manager.

---

## 🔐 Features

- Connects to AWS Secrets Manager
- Retrieves secret by name
- Parses JSON-formatted secrets
- Uses Boto3 SDK and handles errors cleanly

---

## 🧪 Run

```bash
python app.py

# AWS Secrets Manager Demo

This is a simple Python app that securely retrieves secrets from AWS Secrets Manager using the `boto3` SDK. It's designed to demonstrate secure credential handling in a cloud-native environment — a critical component of production-grade DevOps workflows.

## 🔐 Purpose

This project simulates how DevOps engineers handle secret credentials (e.g., API keys, database passwords) securely without hardcoding them into applications. It shows how secrets can be centrally managed and dynamically retrieved at runtime.

## 🧰 Tools Used

- **AWS Secrets Manager**
- **AWS CLI**
- **Python 3**
- **Boto3**
- **Git & GitHub**

## 🚀 How It Works

1. The Python app authenticates using the AWS CLI credentials configured on your machine.
2. It pulls a specified secret from AWS Secrets Manager.
3. The script handles both JSON-formatted and plaintext secrets for flexibility.

## 🧪 Example Output

```bash
$ python app.py
Secret retrieved successfully ✅
Secret content: {'password': 'MySuperSecret123'}
