<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Tohan.Imports</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Inyectamos el estilo Cyber-Tech acá mismo para no depender del CSS global en el login */
        body {
            background-color: #030305;
            color: #ffffff;
        }
        .card-custom {
            background-color: #0d0d12;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .form-control-custom {
            background-color: #1a1a24;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }
        .form-control-custom:focus {
            background-color: #1a1a24;
            border-color: #0066ff;
            color: #ffffff;
            box-shadow: 0 0 0 0.25rem rgba(0, 102, 255, 0.25);
        }
        .btn-tech {
            background-color: #0066ff;
            color: white;
            border: none;
            transition: 0.3s;
        }
        .btn-tech:hover {
            background-color: #0052cc;
            color: white;
        }
        .brand-logo {
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: 1px;
        }
        .brand-logo span {
            color: #0066ff;
        }
    </style>
</head>
<body class="d-flex align-items-center" style="height: 100vh;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-4">
                
                <div class="text-center mb-4">
                    <div class="brand-logo">TOHAN<span>.IMPORTS</span></div>
                </div>

                <div class="card card-custom shadow-lg rounded-4">
                    <div class="card-body p-4">
                        <h5 class="text-center mb-4" style="color: #9ba1a6; font-weight: normal;">Acceso al Panel</h5>
                        
                        {% if error %}
                            <div class="alert text-center" style="background-color: rgba(220, 53, 69, 0.1); border: 1px solid #dc3545; color: #ff6b72;">
                                {{ error }}
                            </div>
                        {% endif %}
                        
                        <form action="/login" method="POST">
                            <div class="mb-3">
                                <label class="form-label" style="color: #9ba1a6; font-size: 0.9rem;">Usuario</label>
                                <input type="text" name="usuario" class="form-control form-control-custom" required autocomplete="off">
                            </div>
                            <div class="mb-4">
                                <label class="form-label" style="color: #9ba1a6; font-size: 0.9rem;">Contraseña</label>
                                <input type="password" name="password" class="form-control form-control-custom" required>
                            </div>
                            <button type="submit" class="btn btn-tech w-100 py-2 rounded-3 fw-bold">Ingresar</button>
                        </form>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</body>
</html>