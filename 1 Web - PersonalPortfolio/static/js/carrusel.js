document.addEventListener('DOMContentLoaded', () => {

    const carruseles = document.querySelectorAll('.proyecto-imagen');

    carruseles.forEach((contenedor) => {

        const imagenes = contenedor.querySelectorAll('.proyecto-slide');
        const indicadores = contenedor.querySelectorAll('.carrusel-indicador');

        const anterior = contenedor.querySelector('.carrusel-prev');
        const siguiente = contenedor.querySelector('.carrusel-next');

        // Si no hay imágenes, no hacemos nada
        if (imagenes.length === 0) {
            return;
        }

        let indiceActual = 0;

        function mostrarImagen(indice) {

            // Si llegamos antes de la primera
            if (indice < 0) {
                indice = imagenes.length - 1;
            }

            // Si llegamos después de la última
            if (indice >= imagenes.length) {
                indice = 0;
            }

            // Mostrar solamente la imagen correspondiente
            imagenes.forEach((imagen, i) => {
                imagen.classList.toggle('active', i === indice);
            });

            // Actualizar los puntos
            indicadores.forEach((indicador, i) => {
                indicador.classList.toggle('active', i === indice);
            });

            indiceActual = indice;
        }

        // Botón anterior
        anterior.addEventListener('click', () => {
            mostrarImagen(indiceActual - 1);
        });

        // Botón siguiente
        siguiente.addEventListener('click', () => {
            mostrarImagen(indiceActual + 1);
        });

        // Indicadores
        indicadores.forEach((indicador, i) => {
            indicador.addEventListener('click', () => {
                mostrarImagen(i);
            });
        });

    });

});
