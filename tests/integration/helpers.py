from contextlib import asynccontextmanager
from firebasil.auth import AuthClient

from gateau_api.service import GateauFirebaseService


@asynccontextmanager
async def temporary_user(
    auth_client: AuthClient,
    email: str,
    password: str,
    display_name: str,
    photo_url: str,
):
    user = await auth_client.sign_up(
        email=email,
        password=password,
    )

    await auth_client.update_profile(
        id_token=user.id_token,
        display_name=display_name,
        photo_url=photo_url,
    )

    try:
        yield user
    finally:
        await auth_client.delete_account(user.id_token)


@asynccontextmanager
async def temporary_service(id_token: str):
    async with GateauFirebaseService(id_token=id_token) as s:
        try:
            yield s
        finally:
            await s.db_root.delete()
