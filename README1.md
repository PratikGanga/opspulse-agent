# OpsPulse: Autonomous Cloud Incident Triage Agent

OpsPulse is an autonomous incident triage and remediation agent powered by **Gemini 3.5**, built with the **Google GenAI SDK**, and deployed on **Google Cloud Run** using **Firestore** for state persistence.

## Mandatory Google Technologies Used
1. **Gemini 3.5**: Multi-step log reasoning and root-cause analysis via `gemini-3.5-pro`.
2. **Google GenAI SDK**: Agentic integration and structured content generation.
3. **Google Cloud Infrastructure**:
   - **Google Cloud Run**: Serverless container hosting and API gateway.
   - **Google Cloud Firestore**: Real-time database for incident tracking and state management.

## Deployment to Google Cloud Run

```bash
# Build and deploy directly to Cloud Run
gcloud run deploy opspulse-agent \
    --source . \
    --region us-central1 \
    --allow-unauthenticated
