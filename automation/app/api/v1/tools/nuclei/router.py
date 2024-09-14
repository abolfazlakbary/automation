from fastapi import APIRouter
from .controller import NucleiController
from core.schema.response import SuccessResponse



nuclei_router = APIRouter(prefix="/nuclei", tags=["Nuclei"])
controller = NucleiController()


@nuclei_router.get(
    "/info",
    summary="Get nuclei info"
)
async def func_get_nuclei_version():
    data = await controller.get_nuclei_version()
    return SuccessResponse.show(data=data)



@nuclei_router.get(
    "/url/scan",
    summary="Nuclei scan for desired url"
)
async def func_scan_site_url(url: str):
    data = await controller.scan_url(url)
    return SuccessResponse.show(data=data)