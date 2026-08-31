from fastapi import APIRouter

from .views.user_views import router as user_router 
from .views.tasks_views import router as task_router 
from .views.profile_views import router as profile_router 

router = APIRouter()

router.include_router(router=user_router, prefix='/user')
router.include_router(router=task_router, prefix='/tasks')
router.include_router(router=profile_router, prefix='/profile')