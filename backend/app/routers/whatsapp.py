from fastapi import APIRouter, HTTPException, Query, Request

from app.core.config import settings

router = APIRouter(prefix="/webhook/whatsapp", tags=["whatsapp"])


@router.get("")
def verify_webhook(
    hub_mode: str = Query(alias="hub.mode"),
    hub_verify_token: str = Query(alias="hub.verify_token"),
    hub_challenge: str = Query(alias="hub.challenge"),
):
    if hub_mode == "subscribe" and hub_verify_token == settings.whatsapp_verify_token:
        return int(hub_challenge)
    raise HTTPException(status_code=403, detail="Verification failed")


@router.post("")
async def receive_message(request: Request):
    payload = await request.json()
    # TODO: pass to the negotiation agent (later ticket)
    return {"received": True}