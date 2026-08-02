// 1. Función para abrir/cerrar el modal con bloqueo de scroll (UX Premium)
function toggleModal() {
    const modal = document.getElementById('modalDiagnostico');
    if (modal) {
        if (modal.style.display === 'flex') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto'; // Habilita el scroll al cerrar
        } else {
            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden'; // Bloquea el scroll al abrir para evitar distracciones
        }
    }
}

// 2. Cerrar el modal al hacer clic fuera del cuadro (Optimizado con addEventListener)
window.addEventListener('click', function(event) {
    const modal = document.getElementById('modalDiagnostico');
    if (event.target === modal) {
        toggleModal();
    }
});

// 3. Lógica de envío unificada (Evita la duplicidad de registros en Admin)
document.addEventListener('DOMContentLoaded', function() {
    const contactoForm = document.getElementById('form-diagnostico');
    
    if (contactoForm) {
        // Importante: Asegúrate de borrar cualquier otro "submit listener" que tengas en el HTML
        contactoForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Evita que la página parpadee o recargue

            const formData = new FormData(this);

            // Envío a la ruta de Flask definida en app.py [2, 3]
            fetch('/contacto', {
                method: 'POST',

                body: formData
            })
            .then(response => {
                if (response.ok) {
                    // Mensaje basado en la promesa de respuesta rápida en menos de 24h [4, 5]
                    alert("Solicitud recibida. Un consultor senior de Panamerican lo contactará en breve.");
                    this.reset();    // Limpia los campos
                    toggleModal();  // Cierra el cuadro automáticamente tras el éxito
                } else {
                    alert("Hubo un error al enviar. Por favor, intente de nuevo o contáctenos por correo.");
                }
            })
            .catch(error => {
                console.error('Error de conexión:', error);
                alert("Error de red. Verifique su conexión e intente nuevamente.");
            });
        });
    }
});

// HCA 20260522 - WHATSAPP - INI 
// Control de visualización inteligente para el botón de WhatsApp
window.addEventListener('scroll', function() {
    const whatsappBtn = document.querySelector('.whatsapp-floating-btn');
    if (whatsappBtn) {
        if (window.scrollY > 250) {
            whatsappBtn.style.opacity = '1';
            whatsappBtn.style.pointerEvents = 'auto';
            whatsappBtn.style.transform = 'scale(1)';
        } else {
            // Se mantiene oculto de manera elegante en el tope del Hero
            whatsappBtn.style.opacity = '0';
            whatsappBtn.style.pointerEvents = 'none';
            whatsappBtn.style.transform = 'scale(0.8)';
        }
    }
});
// Inicializar el estado oculto antes del scroll (añadir al CSS o manejar vía JS)
document.addEventListener("DOMContentLoaded", function() {
    const whatsappBtn = document.querySelector('.whatsapp-floating-btn');
    if (whatsappBtn) {
        whatsappBtn.style.opacity = '0';
        whatsappBtn.style.pointerEvents = 'none';
        whatsappBtn.style.transition = 'all 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
    }
});
// HCA 20260522 - WHATSAPP - FIN 