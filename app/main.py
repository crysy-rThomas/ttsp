from fastapi import Depends, FastAPI

# Include routers after wiring
from routers.document_router import router as document_router
from routers.conversation_router import router as conversation_router
from routers.message_router import router as message_router
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import auth_router
from services.user import UserService

app = FastAPI(
   # swagger_ui_parameters={"persistAuthorization": True},
   # docs_url=None,  # Disable Swagger UI
   # redoc_url=None,  # Disable ReDoc
   # openapi_url=None  # Disable OpenAPI schema
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS", "GET", "DELETE"],  # Allows only POST and OPTIONS
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "FastAPI"}


user_auth_service = UserService()

app.include_router(auth_router)
app.include_router(
    conversation_router,
    prefix="/v0",
    dependencies=[Depends(user_auth_service.get_current_user)],
)

app.include_router(
    message_router,
    prefix="/v0",
    dependencies=[Depends(user_auth_service.get_current_user)],
)


app.include_router(
    document_router,
    prefix="/v0",
    dependencies=[Depends(user_auth_service.get_current_user)],
)
