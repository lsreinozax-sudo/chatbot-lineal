use App\Http\Controllers\ChatbotController;

// Ruta para que el frontend (Vue, React, Blade) pueda preguntar
Route::post('/chatbot/ask', [ChatbotController::class, 'ask'])->name('chatbot.ask');

// Ruta para un panel de administración que verifique el estado
Route::get('/admin/chatbot/health', [ChatbotController::class, 'health'])->name('chatbot.health');