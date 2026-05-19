<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class ChatbotController extends Controller
{
    private $chatbotApiUrl = 'http://chatbot-api:8000';

    public function index()
    {
        return view('chatbot');
    }

    public function ask(Request $request)
    {
        $question = $request->input('question');
        
        if (empty($question)) {
            return response()->json([
                'success' => false,
                'answer' => 'Por favor escribe una pregunta'
            ]);
        }

        try {
            $response = Http::timeout(30)->post($this->chatbotApiUrl . '/query', [
                'question' => $question,
            ]);

            if ($response->successful()) {
                return response()->json([
                    'success' => $response->json('success'),
                    'answer' => $response->json('answer'),
                    'suggestions' => $response->json('suggestions', []),
                ]);
            } else {
                return response()->json([
                    'success' => false,
                    'answer' => 'Error en el servicio de chatbot'
                ]);
            }
        } catch (\Exception $e) {
            return response()->json([
                'success' => false,
                'answer' => 'No se pudo conectar con el chatbot'
            ]);
        }
    }

    public function health()
    {
        try {
            $response = Http::timeout(5)->get($this->chatbotApiUrl . '/health');
            
            if ($response->successful()) {
                return response()->json([
                    'status' => 'online',
                    'data' => $response->json()
                ]);
            } else {
                return response()->json(['status' => 'error']);
            }
        } catch (\Exception $e) {
            return response()->json(['status' => 'offline']);
        }
    }
}