<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>KAVAC Assistant</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="{{ asset('css/chatbot.css') }}">
</head>
<body>
    <div class="chat-container">
        <!-- Header -->
        <div class="chat-header">
            <div class="bot-icon"><i class="fas fa-robot"></i></div>
            <div class="header-text">
                <h2>KAVAC Asistente</h2>
                <span><span class="status-dot"></span> Conectado</span>
            </div>
        </div>
        
        <!-- Botones PRINCIPALES siempre visibles -->
        <div class="quick-actions">
            <button class="quick-btn" onclick="ask('que es kavac')">
                <i class="fas fa-question-circle"></i> ¿Qué es KAVAC?
            </button>
            <button class="quick-btn" onclick="ask('modulos')">
                <i class="fas fa-cubes"></i> Módulos
            </button>
        </div>
        
        <!-- Mensajes -->
        <div class="chat-messages" id="chat-messages">
            <!-- Mensaje de bienvenida SIN sugerencias -->
            <div class="message bot">
                <div>
                    <div class="message-bubble">
                        👋 ¡Hola! Soy el asistente de <strong>KAVAC</strong>. ¿En qué puedo ayudarte?
                    </div>
                    <div class="message-time">Ahora</div>
                </div>
            </div>
        </div>
        
        <!-- Input -->
        <div class="chat-input-wrap">
            <div class="input-group">
                <input type="text" class="chat-input" id="question" placeholder="Escribe tu pregunta..."
                    onkeypress="if(event.key==='Enter') sendQuestion()">
                <button class="send-btn" id="send-btn" onclick="sendQuestion()">
                    <i class="fas fa-paper-plane"></i>
                </button>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $.ajaxSetup({ headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') } });
        
        let isProcessing = false;
        
        function addMessage(sender, text, suggestions = null) {
            const time = new Date().toLocaleTimeString('es', { hour: '2-digit', minute: '2-digit' });
            const isUser = sender === 'user';
            
            let html = `<div class="message ${isUser ? 'user' : 'bot'}"><div>`;
            html += `<div class="message-bubble">${text}</div>`;
            
            // Chips de sugerencia SOLO después de respuestas del bot
            if (!isUser && suggestions && suggestions.length > 0) {
                html += '<div class="suggestions-wrapper">';
                html += '<div class="suggestions-label">También te puede interesar:</div>';
                html += '<div class="suggestions-row">';
                suggestions.forEach(s => {
                    const label = s.replace(/\b\w/g, l => l.toUpperCase()).replace('Kavac', 'KAVAC');
                    const icon = getIcon(s);
                    html += `
                        <button class="suggestion-chip" onclick="ask('${s}')">
                            <span class="chip-icon">${icon}</span> ${label}
                        </button>`;
                });
                html += '</div></div>';
            }
            
            html += `<div class="message-time">${time}</div></div></div>`;
            $('#chat-messages').append(html);
            scrollToBottom();
        }
        
        function getIcon(keyword) {
            if (keyword.includes('kavac') && !keyword.includes('modulo')) return '📚';
            if (keyword.includes('modulo') || keyword.includes('modulos')) return '📦';
            if (keyword.includes('ingresar') || keyword.includes('acceder')) return '🔑';
            if (keyword.includes('contraseña')) return '🔒';
            if (keyword.includes('desarrollo') || keyword.includes('cenditel')) return '🏛️';
            if (keyword.includes('objetivo')) return '🎯';
            if (keyword.includes('talento')) return '👥';
            return '💡';
        }
        
        function addTyping() {
            $('#chat-messages').append(`
                <div class="message bot" id="typing-msg">
                    <div class="message-bubble typing-bubble">
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                    </div>
                </div>
            `);
            scrollToBottom();
        }
        
        function removeTyping() { $('#typing-msg').remove(); }
        
        function scrollToBottom() {
            const c = $('#chat-messages');
            c.scrollTop(c[0].scrollHeight);
        }
        
        function ask(question) {
            $('#question').val(question);
            sendQuestion();
        }
        
        function sendQuestion() {
            const question = $('#question').val().trim();
            if (!question || isProcessing) return;
            
            isProcessing = true;
            $('#send-btn').prop('disabled', true);
            
            addMessage('user', question);
            $('#question').val('');
            addTyping();
            
            $.post('/chatbot/ask', { question: question })
                .done(function(response) {
                    removeTyping();
                    if (response.success) {
                        // Pasa las sugerencias para que aparezcan debajo
                        addMessage('bot', response.answer, response.suggestions);
                    } else {
                        addMessage('bot', '❌ ' + response.answer);
                    }
                })
                .fail(function() {
                    removeTyping();
                    addMessage('bot', '❌ Error de conexión.');
                })
                .always(function() {
                    isProcessing = false;
                    $('#send-btn').prop('disabled', false);
                    $('#question').focus();
                });
        }
    </script>
</body>
</html>