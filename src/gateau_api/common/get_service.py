from gateau_api.service import GateauFirebaseService


async def get_service() -> GateauFirebaseService:
    return GateauFirebaseService()
