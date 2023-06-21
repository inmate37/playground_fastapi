# FastAPI
from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class CreateAttributeRequest(BaseModel):
    attribute: dict


class SetValueRequest(BaseModel):
    value: dict


@app.post('/createAttribute')
async def create_attribute(request: CreateAttributeRequest) -> dict[str, str]:
    attribute = request.attribute
    print(f'Received | Attribute {attribute}')
    return {'message': 'Attribute created successfully'}


@app.post('/setValues')
async def set_values(partner_id: int, user_id: int, request: SetValueRequest) -> dict[str, str]:
    print('\n\n')
    print('\n\n')
    print(partner_id)
    print(user_id)
    print('\n\n')
    print('\n\n')

    value = request.value
    print(
        f'Received | PartnerID {partner_id} | UserID {user_id}: {user_id} '
        f'Name {value.name} | Value {value.value}'
    )
    return {'message': 'Value assigned successfully'}
