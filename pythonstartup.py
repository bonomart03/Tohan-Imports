<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout - Tohan.Imports</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #030305; color: #ffffff; }
        .card-custom { background-color: #0d0d12; border: 1px solid rgba(255, 255, 255, 0.05); }
        .text-muted-custom { color: #9ba1a6 !important; }
        .form-control-custom, .form-select-custom {
            background-color: #1a1a24;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }
        .form-control-custom:focus, .form-select-custom:focus {
            background-color: #1a1a24;
            border-color: #0066ff;
            color: #ffffff;
            box-shadow: 0 0 0 0.25rem rgba(0, 102, 255, 0.25);
        }
        .btn-whatsapp { background-color: #25D366; color: white; font-weight: bold; }
        .btn-whatsapp:hover { background-color: #128C7E; color: white; }
    </style>
</head>
<body class="py-5">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-10">
                
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h2 style="font-weight: 800;">Finalizar Compra</h2>
                    <a href="{{ url_for('catalogo') }}" class="text-decoration-none" style="color: #0066ff;">← Volver al catálogo</a>
                </div>

                {% if carrito %}
                <form action="{{ url_for('procesar_compra') }}" method="POST">
                    <div class="row g-4">
                        
                        <div class="col-lg-6">
                            <div class="card card-custom shadow-lg rounded-4 p-4 h-100">
                                <h4 class="mb-4" style="color: #0066ff;">Datos de Entrega</h4>
                                
                                <div class="mb-3">
                                    <label class="form-label text-muted-custom">Nombre Completo</label>
                                    <input type="text" name="nombre" class="form-control form-control-custom" required>
                                </div>
                                
                                <div class="mb-3">
                                    <label class="form-label text-muted-custom">Teléfono / WhatsApp</label>
                                    <input type="tel" name="telefono" class="form-control form-control-custom" placeholder="Ej: 3513001122" required>
                                </div>
                                
                                <div class="mb-3">
                                    <label class="form-label text-muted-custom">Dirección de Entrega</label>
                                    <input type="text" name="direccion" class="form-control form-control-custom" placeholder="Calle, Número y Piso/Depto" required>
                                </div>
                                
                               <div class="mb-3">
                                    <label class="form-label text-muted-custom">Partido / Zona de Envío</label>
                                    <select name="zona" class="form-select form-select-custom" required>
                                        <option value="" selected disabled>Seleccioná tu zona...</option>
                                        <option value="San Martin">San Martín (Nodo Central - Envío Gratis)</option>
                                        <option value="Villa Ballester">Villa Ballester</option>
                                        <option value="Villa Maipu">Villa Maipú</option>
                                        <option value="Tres de Febrero">Tres de Febrero / Caseros</option>
                                        <option value="CABA Limite">CABA (Zonas limítrofes)</option>
                                        <option value="Otras Zonas GBA">Otras zonas GBA (A coordinar costo)</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="card card-custom shadow-lg rounded-4 p-4 h-100 d-flex flex-column justify-content-between">
                                <div>
                                    <h4 class="mb-4">Resumen de Productos</h4>
                                    <div class="table-responsive">
                                        <table class="table table-dark table-borderless align-middle">
                                            <thead>
                                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                                                    <th>Ítem</th>
                                                    <th class="text-center">Cant.</th>
                                                    <th class="text-end">Subtotal</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {% for id, item in carrito.items() %}
                                                <tr>
                                                    <td>
                                                        <strong>{{ item.nombre }}</strong><br>
                                                        <small class="text-muted-custom">{{ item.marca }}</small>
                                                    </td>
                                                    <td class="text-center">{{ item.cantidad }}</td>
                                                    <td class="text-end">${{ "{:,.2f}".format(item.precio * item.cantidad) }}</td>
                                                </tr>
                                                {% endfor %}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>

                                <div>
                                    <div class="d-flex justify-content-between align-items-center mt-4 pt-3 mb-4" style="border-top: 1px solid rgba(255,255,255,0.1);">
                                        <h4 class="mb-0 text-muted-custom">Total Módulos:</h4>
                                        <h3 class="mb-0" style="color: #0066ff; font-weight: bold;">${{ "{:,.2f}".format(total) }}</h3>
                                    </div>

                                    <div class="d-grid gap-2">
                                        <button type="submit" class="btn btn-whatsapp py-3 rounded-3 shadow-sm">
                                            💾 Confirmar y enviar por WhatsApp
                                        </button>
                                        <a href="{{ url_for('vaciar_carrito') }}" class="btn btn-outline-danger py-2 btn-sm" style="border-color: rgba(220, 53, 69, 0.3); color: #dc3545;">
                                            Vaciar Carrito
                                        </a>
                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>
                </form>
                {% else %}
                <div class="card card-custom shadow-lg rounded-4 p-5 text-center">
                    <h5 class="text-muted-custom mb-3">Tu carrito está completamente vacío</h5>
                    <a href="{{ url_for('catalogo') }}" class="btn py-2 px-4" style="background-color: #0066ff; color: white; font-weight: bold;">Ir al catálogo</a>
                </div>
                {% endif %}

            </div>
        </div>
    </div>
</body>
</html>