result = process_incoming_issue(incoming_issue.model_dump())

        # Replace with your Zapier Webhook URL
webhook_url = "https://hooks.zapier.com/hooks/catch/21371791/2f3clcpzapier_response = requests.post(webhook_url, json=result)

        if zapier_response.status_code == 200:
            return {"message": "Issue processed and sent to Zapier successfully.", "result": result}
        else:
            raise HTTPException(status_code=zapier_response.status_code, detail="Failed to send data to Zapier")
