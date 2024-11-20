import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  TextField,
  Button,
  Typography,
  FormControlLabel,
  Switch,
  Paper,
} from '@mui/material';
import { Save as SaveIcon, ArrowBack as ArrowBackIcon } from '@mui/icons-material';
import api from '../services/api';

function CadastrarPessoa() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    telefone: '',
    data_nascimento: '',
    ativo: true,
  });

  const handleChange = (e) => {
    const { name, value, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'ativo' ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/pessoas/', formData);
      navigate('/');
    } catch (error) {
      console.error('Erro ao cadastrar pessoa:', error);
      alert('Erro ao cadastrar pessoa. Verifique os dados e tente novamente.');
    }
  };

  return (
    <Box sx={{ mt: 4 }}>
      <Box sx={{ mb: 4, display: 'flex', alignItems: 'center', gap: 2 }}>
        <Button
          variant="outlined"
          startIcon={<ArrowBackIcon />}
          onClick={() => navigate('/')}
        >
          Voltar
        </Button>
        <Typography variant="h4" component="h1">
          Cadastrar Nova Pessoa
        </Typography>
      </Box>

      <Paper sx={{ p: 4 }}>
        <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <TextField
            required
            label="Nome"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            fullWidth
          />
          
          <TextField
            required
            label="Email"
            name="email"
            type="email"
            value={formData.email}
            onChange={handleChange}
            fullWidth
          />
          
          <TextField
            label="Telefone"
            name="telefone"
            value={formData.telefone}
            onChange={handleChange}
            fullWidth
          />
          
          <TextField
            required
            label="Data de Nascimento"
            name="data_nascimento"
            type="date"
            value={formData.data_nascimento}
            onChange={handleChange}
            InputLabelProps={{ shrink: true }}
            fullWidth
          />
          
          <FormControlLabel
            control={
              <Switch
                checked={formData.ativo}
                onChange={handleChange}
                name="ativo"
                color="primary"
              />
            }
            label="Ativo"
          />
          
          <Button
            type="submit"
            variant="contained"
            color="primary"
            startIcon={<SaveIcon />}
            sx={{ mt: 2 }}
          >
            Salvar
          </Button>
        </Box>
      </Paper>
    </Box>
  );
}

export default CadastrarPessoa;
