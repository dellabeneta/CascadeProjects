import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';

// Páginas
import ListaPessoas from './pages/ListaPessoas';
import CadastrarPessoa from './pages/CadastrarPessoa';
import EditarPessoa from './pages/EditarPessoa';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Container>
          <Routes>
            <Route path="/" element={<ListaPessoas />} />
            <Route path="/cadastrar" element={<CadastrarPessoa />} />
            <Route path="/editar/:id" element={<EditarPessoa />} />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}

export default App;
