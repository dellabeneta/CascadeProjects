import http from 'k6/http';
import { sleep, check } from 'k6';

// Configuração do teste
export const options = {
  // 50 usuários virtuais
  vus: 50,
  // Duração de 30 segundos
  duration: '30s',
};

// Função que será executada para cada usuário virtual
export default function () {
  // Primeiro faz login para obter o token
  const loginRes = http.post('http://64.227.110.34:8000/auth/token', 
    'username=admin&password=admin',
    {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    }
  );

  // Verifica se o login foi bem sucedido
  check(loginRes, {
    'login successful': (r) => r.status === 200,
    'has access token': (r) => JSON.parse(r.body).access_token !== undefined,
  });

  if (loginRes.status === 200) {
    const token = JSON.parse(loginRes.body).access_token;

    // Faz uma requisição GET para listar pessoas
    const listRes = http.get('http://64.227.110.34:8000/pessoas', {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });

    // Verifica se a listagem foi bem sucedida
    check(listRes, {
      'list successful': (r) => r.status === 200,
    });
  }

  // Espera 1 segundo antes da próxima iteração
  sleep(1);
}
