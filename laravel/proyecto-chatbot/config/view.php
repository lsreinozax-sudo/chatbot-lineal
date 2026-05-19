<!DOCTYPE html>
<html>
<head>
    <title>Chatbot de Documentación</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <meta name="csrf-token" content="{{ csrf_token() }}">
</head>
<body>
    <h2>Asistente de Documentación (Laravel 8)</h2>
    
    <div id="chat-area" style="border:1px solid #ccc; height:300px; overflow-y:scroll; padding:10px; margin-bottom:10px;">
        <p><strong>Asistente:</strong> ¡Hola! Pregúntame sobre la documentación.</p>
    </div>

    <input type="text" id="question" size="80" placeholder="Escribe tu pregunta aquí...">
    <button onclick="askChatbot()">Preguntar</button>
    <p id="loading" style="display:none;">Consultando la documentación...</p>

    <script>
        function askChatbot() {
            let question = $('#question').val();
            if (!question) return;

            // Mostrar mensaje del usuario
            $('#chat-area').append(`<p><strong>Tú:</strong> ${question}</p>`);
            $('#question').val('');
            $('#loading').show();

            $.ajax({
                url: '/chatbot/ask',
                type: 'POST',
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                },
                data: {
                    question: question
                },
                success: function(response) {
                    $('#loading').hide();
                    if (response.success) {
                        $('#chat-area').append(`<p><strong>Asistente:</strong> ${response.answer}</p>`);
                        if (response.sources.length > 0) {
                            $('#chat-area').append(`<p style="color:#777; font-size:0.8em;">Fuentes: ${response.sources.join(', ')}</p>`);
                        }
                    } else {
                        $('#chat-area').append(`<p><strong>Asistente:</strong> ${response.answer}</p>`);
                    }
                    // Scroll al final del chat
                    $('#chat-area').scrollTop($('#chat-area')[0].scrollHeight);
                },
                error: function() {
                    $('#loading').hide();
                    $('#chat-area').append(`<p><strong>Asistente:</strong> Error de conexión con el servicio.</p>`);
                }
            });
        }

        // Enviar con Enter
        $('#question').keypress(function(e) {
            if(e.which == 13) askChatbot();
        });
    </script>
</body>
</html>