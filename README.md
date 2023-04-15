<h1 align="center">
  <a href="#">
    Aplicacion de Pizzas
  </a>
</h1>

<p align="center">
  <strong>Isai jejeje</strong>
</p>

<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens" alt="JWT" />
    </a>
</p>
El proyecto consiste en una rest API con FastAPI implementando autenticacion con JWT, esta consta de varias rutas:
<table style="width:100%">
    <tr>
        <th>Tipo</th>
        <th>Metodo</th>
        <th>Ruta</th>
        <th>Nombre</th>
        <th>Funcion</th>
        <th>Acceso</th>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>POST</em></td>
        <td>place_an_order</td>
        <td>orders/order</td>
        <td>Manda una orden</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>GET</em></td>
        <td>list_all_orders</td>
        <td>/orders/orders</td>
        <td>Obtiene todas las ordenes</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>GET</em></td>
        <td>get_order_by_id</td>
        <td>orders/{id}</td>
        <td>Obtiene la orden con el id especificado</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>GET</em></td>
        <td>get_user_order</td>
        <td>orders/user</td>
        <td>Obtiene las orden del usuario especificado</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>GET</em></td>
        <td>get_specific_order</td>
        <td>orders/user/order/{id}</td>
        <td>Obtiene la orden del usuario loggeado con el id especificado</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>PUT</em></td>
        <td>update_order</td>
        <td>orders/order/update/{id}</td>
        <td>Actuaiza en su totalidad la orden con el id especificado</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>PATCH</em></td>
        <td>update_order_status</td>
        <td>orders/order/update/{id}</td>
        <td>Actualiza el estado de la orden con el id especificado</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Ordenes</td>
        <td><em>DELETE</em></td>
        <td>delete_an_order</td>
        <td>orders/order/delete/{id}</td>
        <td>Elimina la orden con el id especificado</td>
        <td>Restringido</td>
    </tr>
    <tr>
        <td>Usuario</td>
        <td><em>POST</em></td>
        <td>signup</td>
        <td>auth/signup</td>
        <td>Crea una cuenta para el usuario</td>
        <td>Libre</td>
    </tr>
    <tr>
        <td>Usuario</td>
        <td><em>PUT</em></td>
        <td>login</td>
        <td>auth/login</td>
        <td>Inicia sesion del usuario</td>
        <td>Libre</td>
    </tr>
    <tr>
        <td>Usuario</td>
        <td><em>GET</em></td>
        <td>refres_token</td>
        <td>auth/refresh</td>
        <td>Obtiene un token de refresh</td>
        <td>Restringido</td>
    </tr>
</table>