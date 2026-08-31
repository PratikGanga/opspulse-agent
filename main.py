import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from google.genai import types
from google.cloud import firestore

app = FastAPI(title="OpsPulse Incident Triage Agent")

# Initialize Clients
db = firestore.Client()
ai_client = genai.Client()

class AlertPayload(BaseModel):
    alert_id: str
    service_name: str
    error_log: str

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "OpsPulse Agent"}

@app.post("/triage")
def triage_incident(alert: AlertPayload):
    try:
        prompt = f"""
        You are an expert SRE and incident response agent.
        Analyze the following alert log and generate:
        1. Root Cause Analysis (RCA)
        2. Severity Level (Critical, High, Medium, Low)
        3. Step-by-step mitigation commands.

        Service: {alert.service_name}
        Log Details:
        {alert.error_log}
        """

        response = ai_client.models.generate_content(
            model="gemini-3.5-pro",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
            )
        )

        triage_data = {
            "alert_id": alert.alert_id,
            "service": alert.service_name,
            "analysis": response.text,
            "status": "TRIAGED"
        }

        # Persist to Google Cloud Firestore
        db.collection("incidents").document(alert.alert_id).set(triage_data)
        return triage_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
