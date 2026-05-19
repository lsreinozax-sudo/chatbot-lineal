<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ChatbotController;

// Ruta principal de Laravel (ya existe)
Route::get('/', function () {
    return view('welcome');
});

// Rutas del Chatbot
Route::get('/chatbot', [ChatbotController::class, 'index']);
Route::post('/chatbot/ask', [ChatbotController::class, 'ask']);
Route::get('/chatbot/health', [ChatbotController::class, 'health']);
