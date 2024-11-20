import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import { useState, useMemo } from 'react';

// Componentes
import ThemeToggle from './components/ThemeToggle';

// Páginas
import ListaPessoas from './pages/ListaPessoas';
import CadastrarPessoa from './pages/CadastrarPessoa';
import EditarPessoa from './pages/EditarPessoa';

function App() {
  const [mode, setMode] = useState('light');

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode,
          primary: {
            main: '#1976d2',
          },
          secondary: {
            main: '#dc004e',
          },
          background: {
            default: mode === 'light' ? '#ffffff' : '#121212',
            paper: mode === 'light' ? '#ffffff' : '#1e1e1e',
          },
        },
      }),
    [mode]
  );

  const toggleTheme = () => {
    setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <ThemeToggle toggleTheme={toggleTheme} />
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
