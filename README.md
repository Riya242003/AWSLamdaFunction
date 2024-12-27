# AWS Lambda Function with API Gateway for Form

This project demonstrates how to create a simple and efficient contact form using AWS services. When users submit the form, their data is securely stored in DynamoDB through an AWS Lambda function triggered by an API Gateway.

# Features

Serverless Architecture: Fully managed by AWS, ensuring scalability and reliability.

Secure Data Storage: All form data is saved in DynamoDB.

Simple Integration: Easily integrates with any frontend form.

# How It Works

Contact Form: A user fills out the form on a website.

API Gateway: The form data is sent to an API endpoint.

Lambda Function: Processes the data and stores it in DynamoDB.

DynamoDB: Saves the submitted details for further use.

![Alt Text](https://media.geeksforgeeks.org/wp-content/uploads/20231026153053/serverless-authrntication_2-768.jpg)


# Setup Overview

Step 1: Create a DynamoDB Table
I
Set up a DynamoDB table to store the contact form submissions. Use a unique identifier (here I'm using gmail)  as the primary key.

Step 2: Deploy Lambda Function

Write a function to handle form data and integrate it with DynamoDB for data storage.

Step 3: Configure API Gateway

Create an API Gateway endpoint to trigger the Lambda function when the contact form is submitted.

Step 4: Connect Frontend

Build a frontend form that sends user data to the API Gateway endpoint via a POST request.

# Benefits

Ease of Use: Simplified architecture for form handling.

Cost-Effective: Pay only for what you use with AWS services.

Scalable: Automatically handles high traffic without additional setup.




