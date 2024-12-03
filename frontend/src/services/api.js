import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Intercepta todas as requisições
api.interceptors.request.use(config => {
    // Obtém o token do sessionStorage
    const token = sessionStorage.getItem('token');
    
    // Se houver um token, adiciona ele no header
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    
    return config;
}, error => {
    return Promise.reject(error);
});

// Intercepta todas as respostas
api.interceptors.response.use(response => {
    return response;
}, error => {
    if (error.response?.status === 401) {
        // Se receber um 401 (não autorizado), remove o token
        sessionStorage.removeItem('token');
        window.location.href = '/login';
    }
    return Promise.reject(error);
});

export default api;
