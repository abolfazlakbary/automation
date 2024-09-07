from fastapi import APIRouter
from .tools.nuclei.router import nuclei_router
from .tools.recon.router import recon_router


bind_routers = APIRouter(prefix="/api/v1")
bind_routers.include_router(nuclei_router)
bind_routers.include_router(recon_router)