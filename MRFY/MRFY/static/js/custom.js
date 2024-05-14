$(document).ready(function() {
    // Inicializar Select2 en el campo de búsqueda de ingredientes
    $('#Ingredientes').select2({
        placeholder: 'Buscar ingredientes...',
        minimumInputLength: 3,  // Número mínimo de caracteres antes de que aparezcan resultados
        ajax: {
            // URL para recuperar los resultados de la búsqueda
            url: '/buscar_ingredientes/',
            dataType: 'json',
            delay: 250,
            processResults: function(data) {
                return {
                    results: data
                };
            },
            cache: true
        }
    });

    // Manejar el evento de selección de un ingrediente
    $('#Ingredientes').on('select2:select', function(e) {
        var data = e.params.data;
        // Almacenar el ID del ingrediente seleccionado en el campo oculto
        $('#id_ingrediente').val(data.id);
    });
});
