from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from db.models import User, Order
from schemas import OrderModel, OrderStatusModel
from db.database import Session, engine
from fastapi.encoders import jsonable_encoder

order_router=APIRouter(prefix="/orders", tags=["orders"])
session=Session(bind=engine)

@order_router.get("/")
async def hello(Authorize:AuthJWT=Depends()):
    """
        ## Ruta de prueba para la autenticacion
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token")
    return {"message":"hello order"}

@order_router.post("/order", status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderModel, Authorize:AuthJWT=Depends()):
    """
        ## Agrega una nueva orden (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token")
    current_user=Authorize.get_jwt_subject()
    user=session.query(User).filter(User.username==current_user).first()
    new_order=Order(
        pizza_size=order.pizza_size,
        quantity=order.quantity
    )
    new_order.user=user
    session.add(new_order)
    session.commit()
    response={
        "pizza_size":new_order.pizza_size,
        "quantity":new_order.quantity,
        "id":new_order.id,
        "order_staus":new_order.order_status
    }
    return jsonable_encoder(response)

@order_router.get("/orders")
async def list_all_orders(Authorize:AuthJWT=Depends()):
    """
        ## Muestra todas las ordenes (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )
    current_user=Authorize.get_jwt_subject()
    user=session.query(User).filter(User.username==current_user).first()
    if(user.is_staff):
        orders=session.query(Order).all()
        return jsonable_encoder(orders)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not a superuser")

@order_router.get("/order/{id}")
async def get_order_by_id(id:int, Authorize:AuthJWT=Depends()):
    """
        ## Regresa una orden con el id correspondiente (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
            )
    user=Authorize.get_jwt_subject()
    current_user=session.query(User).filter(User.username==user).first()
    if(current_user.is_staff):
        order=session.query(Order).filter(Order.id==id).first()
        return jsonable_encoder(order)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are not a superuser")

@order_router.get("/user/orders")
async def get_user_orders(Authorize:AuthJWT=Depends()):
    """
        ## Muestra todas las ordenes hechas por un usuario (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )
    user=Authorize.get_jwt_subject()
    current_user=session.query(User).filter(User.username==user).first()
    return jsonable_encoder(current_user.orders)

@order_router.get("/user/order/{id}")
async def get_specific_order(id:int, Authorize:AuthJWT=Depends()):
    """
        ## Muestra la orden con el id especificado del usuario loggeado (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )
    user=Authorize.get_jwt_subject()
    current_user=session.query(User).filter(User.username==user).first()
    orders=current_user.orders
    for order in orders:
        if(order.id==id):
            return jsonable_encoder(order)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="No order with such id"
    )

@order_router.put("/order/update/{id}")
async def update_order(id:int, order:OrderModel, Authorize:AuthJWT=Depends()):
    """
        ## Actualiza una orden (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )
    order_to_update=session.query(Order).filter(Order.id==id).first()
    order_to_update.quantity=order.quantity
    order_to_update.pizza_size=order.pizza_size
    session.commit()
    response={
        "id":order_to_update.id,
        "quantity":order_to_update.quantity,
        "pizza_size":order_to_update.pizza_size,
        "order_status":order_to_update.order_status
    }
    return jsonable_encoder(response)

@order_router.patch("/order/update/{id}")
async def update_order_status(id:int,
                            order:OrderStatusModel,
                            Authorize:AuthJWT=Depends()):
    """
        ## Actualiza el status de una orden (Requiere autentificacion y super usuario)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )
    username=Authorize.get_jwt_subject()
    current_user=session.query(User).filter(User.username==username).first()
    if(current_user.is_staff):
        order_to_update=session.query(Order).filter(Order.id==id).first()
        order_to_update.order_status=order.order_status
        session.commit()
        response={
                "id":order_to_update.id,
                "quantity":order_to_update.quantity,
                "pizza_size":order_to_update.pizza_size,
                "order_status":order_to_update.order_status
            }
        return jsonable_encoder(response)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid token"
    )
    
@order_router.delete("/order/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_an_order(id:int, Authorize:AuthJWT=Depends()):
    """
        ## Elimina una orden por id (Requiere autentificacion)
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )
    order_to_delete=session.query(Order).filter(Order.id==id).first()
    session.delete(order_to_delete)
    session.commit
    return order_to_delete

"""
    Que pasa si no encuentra al usuario a la hora de poner una orden: manda un "token invalido" ✅
   
"""
    
    