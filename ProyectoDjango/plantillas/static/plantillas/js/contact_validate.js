$(document).ready(function () {
    // Validación del formulario
    $("#contactForm").validate({
        rules: {
            nombre: "required",
            correo: {
                required: true,
                correo: true
            },
            mensaje: "required"
        },
        messages: {
            nombre: "Por favor, ingrese su nombre completo",
            correo: {
                required: "Por favor, ingrese su correo electrónico",
                correo: "Por favor, ingrese un correo electrónico válido"
            },
            mensaje: "Por favor, ingrese su mensaje"
        },
    });
});