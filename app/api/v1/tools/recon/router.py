from fastapi import APIRouter
from .controller import ReconController
from core.schema.response import SuccessResponse



recon_router = APIRouter(prefix="/recon", tags=["Recon"])
controller = ReconController()


@recon_router.get(
    "/subenum/info",
    summary="Get SubEnum info"
)
async def func_get_subenum_info():
    data = await controller.get_subenum_info()
    return SuccessResponse.show(data=data)


@recon_router.get(
    "/subenum/search",
    summary="Search a domain with SubEnum"
)
async def func_search_with_subenum(domain: str):
    data = await controller.subenum_search(domain)
    return SuccessResponse.show(data=data)
