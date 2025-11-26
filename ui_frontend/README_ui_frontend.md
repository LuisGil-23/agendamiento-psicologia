# ui_frontend (Django-ready)
Esto es una aplicación Django 'standalone' con las vistas y plantillas modernas para:
- Login (para psicólogas y usuarios)
- Pantalla de inicio (home)
- Lista de psicólogas disponibles
- Lista de citas

**Cómo integrarlo en tu proyecto existente** (sin cambiar la lógica ya implementada):
1. Copia la carpeta `ui_frontend` al root de tu proyecto (junto a manage.py).
2. Asegúrate de que `django.contrib.staticfiles` esté en INSTALLED_APPS y `STATICFILES_DIRS`/`STATIC_ROOT` esté configurado.
3. Añade en tu `settings.py` la carpeta de templates si es necesario, o usa las plantillas incluidas así:
   - Si las plantillas no son detectadas, agrega al `TEMPLATES[0]['DIRS']` la ruta `os.path.join(BASE_DIR, 'templates')`.
4. Incluir las URLs en tu `urls.py` principal:
   ```py
   from django.urls import include, path
   urlpatterns += [ path('ui/', include('ui_frontend.urls', namespace='ui_frontend')) ]
   ```
5. Ejecuta `python manage.py collectstatic` si sirves estáticos en producción o configura tu servidor web para apuntar a `static/`.
6. Las vistas intentan importar modelos existentes (`psicologas.models.Psicologa`, `citas.models.Cita`). Si esos modelos existen, las plantillas mostrarán datos reales. Si no, se muestran datos de ejemplo para diseño.
7. Personaliza colores y textos en `static/ui_frontend/style.css` y las plantillas HTML.

Si quieres, puedo generar un `commit` (diff) para añadir esto automáticamente dentro del repo que subiste — para eso necesitaría extraer y reempaquetar el proyecto. Actualmente no pude modificar directamente el .rar porque falta la utilidad `unrar` en este entorno. Te entrego el paquete listo para que lo incorpores manualmente o me indiques que lo integre directamente en el repo y lo haga por ti.
