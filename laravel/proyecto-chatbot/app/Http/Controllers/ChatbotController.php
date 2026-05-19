<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Illuminate\Http\JsonResponse;

class ChatbotController extends Controller
{
    // La URL donde corre tu API de FastAPI
    private $chatbotApiUrl = 'http://127.0.0.1:8000';

    /**
     * Endpoint para preguntar al chatbot (usado por AJAX desde el frontend)
     */
    public function ask(Request $request): JsonResponse
    {
        $request->validate([
            'question' => 'required|string|min:3',
        ]);

        try {
            $response = Http::timeout(60)->post($this->chatbotApiUrl . '/query', [
                'question' => $request->input('question'),
                'top_k' => 3,
            ]);

            if ($response->successful()) {
                return response()->json([
                    'success' => true,
                    'answer' => $response->json('answer'),
                    'sources' => $response->json('sources'),
                ]);
            } else {
                \log::error('Error en API del chatbot', ['status' => $response->status(), 'body' => $response->body()]);
                return response()->json([
                    'success' => false,
                    'answer' => 'Lo siento, el servicio de documentación no está disponible en este momento.',
                ], 503);
            }

        } catch (\Exception $e) {
            \log::error('Excepción al conectar con API del chatbot: ' . $e->getMessage());
            return response()->json([
                'success' => false,
                'answer' => 'No se pudo conectar con el asistente de documentación. Asegúrate de que el servicio esté activo.',
            ], 503);
        }
    }

    /**
     * Endpoint simple para verificar el estado del servicio desde Laravel
     */
    public function health(): JsonResponse
    {
        try {
            $response = Http::timeout(5)->get($this->chatbotApiUrl . '/health');
            $data = $response->json();
            return response()->json([
                'status' => 'OK',
                'chunks_loaded' => $data['chunks_in_db'] ?? 0
            ]);
        } catch (\Exception $e) {
            return response()->json(['status' => 'Error', 'message' => $e->getMessage()], 503);
        }
    }
}