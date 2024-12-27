import json
import boto3

def lambda_handler(event, context):
   
    try:
        mypage = page_router(event['httpMethod'], event['queryStringParameters'],json.loads(event['body']) if event['body'] else {} )
        return mypage
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def page_router(httpmethod, querystring, formbody):
    
    if httpmethod == 'GET':
        try:
            with open('contactus.html', 'r') as htmlFile:
                htmlContent = htmlFile.read()
            return {
                'statusCode': 200,
                'headers': {"Content-Type": "text/html"},
                'body': htmlContent
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

    elif httpmethod == 'POST':
        try:
            
            insert_record(formbody)
            with open('success.html', 'r') as htmlFile:
                htmlContent = htmlFile.read()
            return {
                'statusCode': 200,
                'headers': {"Content-Type": "text/html"},
                'body': htmlContent
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

def insert_record(formbody):
    
    try:
        
        formbody = "INSERT INTO RiyaDemoTable value "+"{"+ f"'fname':'{formbody['fname']}','last':'{formbody['lname']}','email':'{formbody['email']}','message':'{formbody['message']}'"+"}";
       

        client = boto3.client('dynamodb')
        response = client.execute_statement(Statement=formbody)
    # Assuming the execute_statement call returns successfully
      
        return response

    except Exception as e:
       
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
             
        }