import json
import boto3
import os

sns_client = boto3.client("sns")


def handler(event, _context):
    body = json.loads(event.get("body"))

    allowed_sites = [
        "https://www.venkkatr.com",
        "http://www.venkkatr.com",
        "http://venkkatr.com",
        "https://venkkatr.com",
    ]

    if event["headers"]["origin"] in allowed_sites:
        allowed_url = event["headers"]["origin"]

    sns_client.publish(
        TopicArn=os.getenv("SNS_TOPIC"),
        Message=" Name: {name} \n Phone: {phone} \n Email: {email} \n Message: {message}".format(
            name=body["name"],
            phone=body["phone"],
            email=body["email"],
            message=body["message"],
        ),
        Subject=body["subject"],
    )
    return {
        "statusCode": 200,
        "headers": {
            "x-custom-header": "contact_header",
            "Access-Control-Allow-Origin": allowed_url,
        },
        "body": json.dumps({"success": "success"}),
    }
