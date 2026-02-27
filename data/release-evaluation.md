## 4. Actividades desarrolladas

### 4.1 Atributos de calidad críticos
Para este sistema, consideramos tres atributos clave:

- **Fiabilidad:** El sistema debe funcionar sin fallas al agendar citas. Un fallo podría afectar la atención médica.  
- **Seguridad:** Es necesario proteger los datos de los pacientes y asegurar que solo personal autorizado pueda acceder a la información.  
- **Usabilidad:** Pacientes y doctores deben poder usar el sistema de manera sencilla y rápida, evitando errores al reservar citas.

### 4.2 Hallazgos
Identificamos seis hallazgos que afectan la calidad:
### 4.2 Identificación de hallazgos
Se identificaron seis hallazgos relacionados con la calidad del software:

1. **Endpoint `/appointments` falla si no hay citas**  
   - **Atributo afectado:** Fiabilidad  
   - **Riesgo:** El sistema puede colapsar al intentar crear la primera cita  
   - **Impacto:** Alto  
   - **Probabilidad:** Media

2. **No hay validación de formato de fecha/hora**  
   - **Atributo afectado:** Fiabilidad  
   - **Riesgo:** La aplicación puede aceptar fechas incorrectas  
   - **Impacto:** Medio  
   - **Probabilidad:** Alta

3. **No hay autenticación de usuarios médicos**  
   - **Atributo afectado:** Seguridad  
   - **Riesgo:** Datos de pacientes podrían ser accedidos por personas no autorizadas  
   - **Impacto:** Alto  
   - **Probabilidad:** Media

4. **Mensajes de error poco claros**  
   - **Atributo afectado:** Usabilidad  
   - **Riesgo:** Los usuarios no entienden qué está mal  
   - **Impacto:** Medio  
   - **Probabilidad:** Alta

5. **Interfaz no adapta bien nombres con acentos**  
   - **Atributo afectado:** Usabilidad  
   - **Riesgo:** Errores en nombres de doctores con caracteres especiales  
   - **Impacto:** Bajo  
   - **Probabilidad:** Media

6. **Falta de logs de actividad**  
   - **Atributo afectado:** Fiabilidad  
   - **Riesgo:** Difícil rastrear errores y fallos  
   - **Impacto:** Medio  
   - **Probabilidad:** Media

### 4.3 Evaluación de riesgo
Se evaluó el impacto y la probabilidad de cada hallazgo, clasificando la severidad:

- Endpoint `/appointments` falla si no hay citas → **Alta**  
- No hay validación de formato de fecha/hora → **Media**  
- No hay autenticación de usuarios médicos → **Alta**  
- Mensajes de error poco claros → **Media**  
- Interfaz no adapta bien nombres con acentos → **Baja**  
- Falta de logs de actividad → **Media**

### 4.4 Decisión de Release (Go / No-Go)
**Decisión:** **Go con observaciones**

**Justificación:**  
El sistema cumple su función principal de gestionar citas médicas y el endpoint `/health` confirma que el servidor está activo. Los hallazgos identificados no bloquean completamente la operación, pero requieren seguimiento y corrección en próximas versiones, como la validación de fechas, la autenticación de usuarios y el manejo correcto de nombres con acentos. Por lo tanto, se puede liberar este release a producción considerando las observaciones y riesgos señalados.